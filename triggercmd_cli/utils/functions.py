import json
import os
import subprocess
from pathlib import Path
from typing import List, Union

from triggercmd_cli.utils import constants, exceptions
from triggercmd_cli import __version__


def load_json_file(path: Union[Path, str] = constants.COMMAND_FILE_PATH) -> List[dict]:
    with open(path, "r", encoding="utf-8") as json_file:
        return json.load(json_file)


def update_json_file(data: List[dict]):
    with os.fdopen(os.open(constants.COMMAND_FILE_PATH, os.O_WRONLY | os.O_CREAT, 0o600), 'w', encoding="utf-8") as json_file:
        json_file.seek(0)
        json_file.write(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))
        json_file.truncate()


def get_command_titles():
    return [command["trigger"] for command in load_json_file()]


def get_command_by_trigger(trigger):
    for command in load_json_file():
        if command["trigger"] == trigger:
            return command
    raise exceptions.CommandNotExist


def get_token_by_file():
    try:
        with open(constants.TOKEN_PATH) as tokenfile:
            return tokenfile.read()
    except Exception:
        raise exceptions.TokenFileNotFound


def generate_shortcut(destiny_path: Union[str, Path]):
    template = """
    [Desktop Entry]
    Version={version}
    Type=Application
    Name=TriggerCMD App
    Comment=TriggerCMD Desktop Application
    Exec=sh -c "triggercmd app"
    Icon={icon_path}
    Path=
    Terminal=false
    StartupNotify=true
    """

    with open(destiny_path, "w+") as file:
        file.write(
            template.format(
                version=__version__,
                icon_path=str(Path.home() / Path('TRIGGERcmd-Agent/src/iconico.ico'))
            )
        )
