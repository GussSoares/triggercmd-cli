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
