class CommandNotExist(Exception):
    def __init__(self, *args: object) -> None:
        default_message = "This command does not exist!"
        super().__init__(default_message, *args)


class TokenFileNotFound(Exception):
    def __init__(self, *args: object) -> None:
        default_message = "Token file has not founded in .TRIGGERcmdData/ folder"
        super().__init__(default_message, *args)


class NotInstalled(Exception):
    def __init__(self, *args: object) -> None:
        default_message = "TriggerCMD is not installed. Please type `triggercmd install` to install TriggerCMD Agent."
        super().__init__(default_message, *args)


class AlreadyCloned(Exception):
    def __init__(self, *args: object) -> None:
        default_message = "TriggerCMD is already cloned."
        super().__init__(default_message, *args)


class AlreadyInstalled(Exception):
    def __init__(self, *args: object) -> None:
        default_message = "TriggerCMD is already installed."
        super().__init__(default_message, *args)
