import os

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from triggercmd_cli.command.entities import Command
from triggercmd_cli.api.schemas import Command as CommandSchema
from triggercmd_cli.utils.file import JsonFile
from triggercmd_cli.utils import constants

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/commands")
def get_commands():
    return JSONResponse(JsonFile.load(constants.COMMAND_FILE_PATH), status_code=200)


@app.get("/command")
def get_commands(search: str = None):
    """
    It returns a list of commands that match the search term

    :param search: str = None
    :type search: str
    :return: A JSONResponse object with the data from the command file.
    """

    if search:
        result = [
            item
            for item in JsonFile.load(constants.COMMAND_FILE_PATH)
            if search.lower() in item.get("trigger").lower()
        ]
        return JSONResponse(result, status_code=200)
    else:
        return JSONResponse(JsonFile.load(constants.COMMAND_FILE_PATH), status_code=200)


@app.post("/command")
def create_command(command: CommandSchema):
    """
    Create a new command

    :param command: CommandSchema
    :type command: CommandSchema
    :return: A JSONResponse object with a message and a status code.
    """

    Command.new(**command.dict())
    return JSONResponse({"msg": "Command created"}, status_code=200)


@app.patch("/command")
def edit_command(old_title: str, command: CommandSchema):
    """
    It takes a string and a CommandSchema object, and then edits the command with the old title to the new command

    :param old_title: The title of the command you want to edit
    :type old_title: str
    :param command: CommandSchema - This is the new command that will be used to replace the old one
    :type command: CommandSchema
    :return: A JSONResponse object with a message and a status code.
    """

    Command.edit(old_title, command.dict())
    return JSONResponse({"msg": "Command edited"}, status_code=200)


@app.delete("/command")
def delete_command(command: CommandSchema):
    """
    It deletes a command from the database

    :param command: CommandSchema - this is the parameter that will be passed to the function
    :type command: CommandSchema
    :return: A JSONResponse object with a message and a status code.
    """

    Command.remove(command.dict())
    return JSONResponse({"msg": "Command removed"}, status_code=200)


@app.get("/test-command") 
def test_command(trigger: str):
    """
    It takes a trigger as a parameter, calls the test function in the Command class, and returns a JSON response with the
    message and status code

    :param trigger: The trigger word for the command
    :type trigger: str
    :return: A JSONResponse object with a dictionary containing a key "msg" and a value of the message variable.
    """

    response, status = Command.test("lenovo", trigger)
    if status == 200:
        message = response.get('message')
    else:
        message = response.get('error')
    return JSONResponse({"msg": message}, status_code=status)

parent_dir_path = os.path.dirname(os.path.realpath(__file__))
app.mount("/", StaticFiles(directory=f"{parent_dir_path}/static", html=True), name="static")
