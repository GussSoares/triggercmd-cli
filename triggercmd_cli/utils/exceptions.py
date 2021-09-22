class CommandNotExist(Exception):
    def __init__(self, *args: object) -> None:
        default_message = "This command does not exist!"
        super().__init__(default_message, *args)


class TokenFileNotFound(Exception):
    def __init__(self, *args: object) -> None:
        default_message = "Token file has not founded in .TRIGGERcmdData/ folder"
        super().__init__(default_message, *args)
