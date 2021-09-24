import os
import subprocess
from pathlib import Path
from typing import Tuple

import requests

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
        command = functions.get_command_by_trigger(trigger)

        for com in functions.load_json_file():
            if com["trigger"] == command["trigger"]:
                commands.remove(com)
                commands.append(new_data)

        functions.update_json_file(commands)

    @staticmethod
    def remove(command: dict):
        commands = functions.load_json_file()
        for com in functions.load_json_file():
            if com["trigger"] == command["trigger"]:
                commands.remove(com)
        functions.update_json_file(commands)

    @staticmethod
    def test(computer_name: str, trigger_name: str):
        return TriggerCMDAPI.run_command(computer_name, trigger_name)


class TriggerCMDAgent:
    @staticmethod
    def clone():
        os.chdir(Path.home() / Path("Sandbox"))
        if Path(Path.home() / Path("Sandbox/TRIGGERcmd-Agent")).exists():
            raise exceptions.AlreadyCloned

        subprocess.run(
            args=f"git clone {constants.REPO_TRIGGERCMD_AGENT}", shell=True,
        )

    @staticmethod
    def install_dependecies():
        constants.BASE_PATH_AGENT
        os.chdir(Path.home() / Path("Sandbox"))
        if Path(Path.home() / Path("Sandbox/TRIGGERcmd-Agent")).exists():
            subprocess.run(
                args=f"yarn",
                shell=True,
            )
        else:
            raise exceptions.NotInstalled

    @staticmethod
    def run():
        if Path(Path.home() / Path("TRIGGERcmd-Agent")).exists():
            subprocess.run(
                "node ~/TRIGGERcmd-Agent/src/agent.js --console", shell=True
            )
        else:
            raise exceptions.NotInstalled


class TriggerCMDAPI:
    URL = "https://triggercmd.com"

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
