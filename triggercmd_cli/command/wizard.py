from typing import List

from InquirerPy import inquirer

from triggercmd_cli.utils import functions


class CommandWizard:
    @staticmethod
    def new():
        return {
            "trigger": inquirer.text(
                message="Type the command name:",
                default="",
                validate=lambda v: len(v) > 0,
            ).execute(),
            "command": inquirer.text(
                message="Type the command:",
                default="",
                validate=lambda v: len(v) > 0,
            ).execute(),
            "ground": inquirer.select(
                message="Type the command ground:",
                choices=["foreground", "background"],
            ).execute(),
            "voice": inquirer.text(
                message="Type the command voice:",
                default="",
                validate=lambda v: len(v) > 0,
            ).execute(),
            "allowParams": inquirer.select(
                message="Allow Params?",
                choices=["false", "true"],
            ).execute(),
        }

    @staticmethod
    def edit(initial: dict):
        return {
            "trigger": inquirer.text(
                message="Type the command name:",
                default=initial["trigger"],
                validate=lambda v: len(v) > 0,
            ).execute(),
            "command": inquirer.text(
                message="Type the command:",
                default=initial["command"],
                validate=lambda v: len(v) > 0,
            ).execute(),
            "ground": inquirer.select(
                message="Select a command ground:",
                choices=["foreground", "background"],
                default=initial["ground"],
            ).execute(),
            "voice": inquirer.text(
                message="Type the command voice:",
                default=initial["voice"],
                validate=lambda v: len(v) > 0,
            ).execute(),
            "allowParams": inquirer.select(
                message="Allow Params?",
                default=initial["allowParams"],
                choices=["false", "true"],
            ).execute(),
        }

    @staticmethod
    def select_command(options: List[str]):
        return functions.get_command_by_trigger(
            inquirer.select(
                message="Select a command:",
                choices=options,
            ).execute()
        )

    @staticmethod
    def confirm(message: str):
        return inquirer.confirm(message).execute()
