from typing import Tuple

import requests

from triggercmd_cli.utils import functions


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
