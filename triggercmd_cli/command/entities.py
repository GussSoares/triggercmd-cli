import os
import platform
import subprocess
import multiprocessing
import shutil
from pathlib import Path
from typing import Tuple

import requests
import uvicorn

from triggercmd_cli import __version__
from triggercmd_cli.command.webview import PythonWebView
from triggercmd_cli import settings
from triggercmd_cli.utils import constants, exceptions, functions


class Command:
    @staticmethod
    def new(trigger, command, ground, voice, allowParams):
        commands = functions.load_json_file()
        commands.append(
            {
                "trigger": trigger,
                "command": command,
                "ground": ground,
                "voice": voice,
                "allowParams": allowParams,
            }
        )
        functions.update_json_file(commands)

    @staticmethod
    def edit(trigger, new_data):
        """
        >>> new_data = {
            "trigger": "test",
            "command": "echo test",
            "ground": "foreground",
            "voice": "test",
            "allowParams": False
        }
        """
        commands = functions.load_json_file()
        # command = functions.get_command_by_trigger(trigger)

        for com in commands:
            if com["trigger"] == trigger:
                commands.remove(com)
                commands.append(new_data)
                break

        functions.update_json_file(commands)

    @staticmethod
    def remove(command: dict):
        commands = functions.load_json_file()
        for com in commands:
            if com["trigger"] == command["trigger"]:
                commands.remove(com)
                break
        functions.update_json_file(commands)

    @staticmethod
    def test(computer_name: str, trigger_name: str):
        return TriggerCMDAPI.run_command(computer_name, trigger_name)

    @staticmethod
    def uninstall():
        return "Please type \"pip uninstall triggercmd\""


class TriggerCMDAgent:
    @staticmethod
    def clone():
        if platform.system() == "Linux":
            current_path = os.getcwd()
            os.chdir(Path("/usr/share/"))
            if Path("TRIGGERcmd-Agent").exists():
                raise exceptions.AlreadyCloned

            subprocess.run(
                args=f"git clone {constants.REPO_TRIGGERCMD_AGENT}", shell=True,
            )
            os.chdir(current_path)
        else:
            raise exceptions.OSNotSupported

    @staticmethod
    def install_dependecies():
        if platform.system() == "Linux":
            current_path = os.getcwd()
            os.chdir(Path.home())
            if Path(Path.home() / Path("TRIGGERcmd-Agent")).exists():
                subprocess.run(
                    args=f"yarn",
                    shell=True,
                )
                os.chdir(current_path)
            else:
                raise exceptions.NotInstalled
        else:
            raise exceptions.OSNotSupported

    @staticmethod
    def run():
        if platform.system() == "Linux":
            if Path(Path.home() / Path("TRIGGERcmd-Agent")).exists():
                try:
                    subprocess.call(
                        "node ~/TRIGGERcmd-Agent/src/agent.js --console",
                        shell=True,
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.STDOUT,
                        start_new_session=True
                    )
                except KeyboardInterrupt:
                    print("Exiting...")
            else:
                raise exceptions.NotInstalled
        else:
            raise exceptions.OSNotSupported

    @staticmethod
    def exit():
        subprocess.run("pkill -9 -f \"agent.js --console\"", shell=True)

    @staticmethod
    def uninstall():
        if platform.system() == "Linux":
            current_path = os.getcwd()
            os.chdir(Path.home())
            if Path(Path.home() / Path("TRIGGERcmd-Agent")).exists():
                shutil.rmtree(Path.home() / Path("TRIGGERcmd-Agent"))
                os.chdir(current_path)
            else:
                raise exceptions.NotInstalled
        else:
            raise exceptions.OSNotSupported

class TriggerCMDAPI:
    URL: str = "https://triggercmd.com"

    @staticmethod
    def get_header():
        return {
            "Authorization": f"Bearer {functions.get_token_by_file()}",
            "Content-Type": "application/json",
        }

    @staticmethod
    def get(url: str, **kwargs):
        return requests.request(
            method="GET", url=f"{TriggerCMDAPI.URL}/{url}", **kwargs
        )

    @staticmethod
    def post(url: str, **kwargs):
        return requests.request(
            method="POST", url=f"{TriggerCMDAPI.URL}/{url}", **kwargs
        )

    @staticmethod
    def run_command(computer_name: str, trigger_name: str) -> Tuple[dict, int]:
        result = TriggerCMDAPI.post(
            url="api/run/triggerSave",
            json={
                "computername": computer_name,
                "triggername": trigger_name,
            },
            headers=TriggerCMDAPI.get_header(),
        )
        return result.json(), result.status_code
    
    @staticmethod
    def login(email: str, password: str) -> Tuple[dict, int]:
        result = TriggerCMDAPI.post(
            url="api/auth/authenticate",
            json={
                "email": email,
                "password": password,
            },
            headers=TriggerCMDAPI.get_header(),
        )
        return result.json(), result.status_code


class TriggerCMDUI:
    def __init__(self):
        self.thread_api = None
        self.thread_agent = None

    def start_uvicorn(self, *args, **kwargs):
        uvicorn.run(
            app='triggercmd_cli.api.main:app',
            host=settings.DEFAULT_HOST,
            port=settings.DEFAULT_PORT,
            log_level='critical'
        )

    def start_agent(self, *args, **kwargs):
        if not self.thread_agent:
            self.thread_agent = multiprocessing.Process(target=TriggerCMDAgent.run)
            self.thread_agent.start()

    def start_api(self, *args, **kwargs):
        if not self.thread_api:
            self.thread_api = multiprocessing.Process(target=self.start_uvicorn)
            self.thread_api.start()

    def stop_api(self, *args, **kwargs):
        if self.thread_api:
            self.thread_api.terminate()

    def stop_agent(self, *args, **kwargs):
        if self.thread_agent:
            self.thread_agent.terminate()

    def ui(self, *args, **kwargs):
        PythonWebView(
            url=f"{settings.DEFAULT_METHOD}{settings.DEFAULT_HOST}:{settings.DEFAULT_PORT}",
            background=kwargs.pop("background"),
            methods={
            "create": [
                self.start_api
            ],
            "quit": [
                self.stop_api,
                self.stop_agent,
                TriggerCMDAgent.exit
            ]
        }).run()

    def start_app(self, *args, **kwargs):
        self.start_api()
        self.start_agent()
        self.ui(
            background=kwargs.pop("background")
        )

    @staticmethod
    def create_shortcut(*args, **kwargs):
        template = """
    [Desktop Entry]
    Version={version}
    Type=Application
    Name=TriggerCMD App
    Comment=TriggerCMD Desktop Application
    Exec=sh -c "$(which triggercmd) app"
    Icon={icon_path}
    Path=
    Terminal=false
    StartupNotify=true
    """
        destiny = Path.home() / Path('.local/share/applications/triggercmd.desktop')
        os.umask(0)
        with open(os.open(destiny, os.O_CREAT | os.O_WRONLY, 0o777), 'w') as fh:
            fh.write(
                template.format(
                    version=__version__,
                    icon_path=str(Path.home() / Path('TRIGGERcmd-Agent/src/iconico.ico'))
                )
            )

    @staticmethod
    def remove_shortcut(*args, **kwargs):
        if Path(
            Path.home() / Path('.local/share/applications/triggercmd.desktop')
        ).exists():
            os.remove(Path.home() / Path('.local/share/applications/triggercmd.desktop'))
