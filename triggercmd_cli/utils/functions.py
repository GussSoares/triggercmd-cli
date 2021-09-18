import json
from pathlib import Path
from typing import List, Union

from triggercmd_cli.utils import exceptions
from triggercmd_cli.utils.constants import COMMAND_FILE_PATH


def load_json_file(path: Union[Path, str] = COMMAND_FILE_PATH) -> List[dict]:
    with open(path) as json_file:
        return json.load(json_file)


def update_json_file(data: List[dict]):
    with open(COMMAND_FILE_PATH, "w+") as json_file:
        json_file.write(json.dumps(data, indent=4, sort_keys=True))


def get_command_titles():
    return [command["trigger"] for command in load_json_file()]


def get_command_by_trigger(trigger):
    for command in load_json_file():
        if command["trigger"] == trigger:
            return command
    raise exceptions.CommandNotExist
