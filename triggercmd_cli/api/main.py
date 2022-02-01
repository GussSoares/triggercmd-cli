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
    Command.new(**command.dict())
    return JSONResponse({"msg": "Command created"}, status_code=200)


@app.patch("/command")
def edit_command(old_title: str, command: CommandSchema):
    Command.edit(old_title, command.dict())
    return JSONResponse({"msg": "Command edited"}, status_code=200)


@app.delete("/command")
def delete_command(command: CommandSchema):
    Command.remove(command.dict())
    return JSONResponse({"msg": "Command removed"}, status_code=200)


@app.get("/test-command") 
def test_command(trigger: str):
    response, status = Command.test("lenovo", trigger)
    if status == 200:
        message = response.get('message')
    else:
        message = response.get('error')
    return JSONResponse({"msg": message}, status_code=status)

parent_dir_path = os.path.dirname(os.path.realpath(__file__))
app.mount("/", StaticFiles(directory=f"{parent_dir_path}/static", html=True), name="static")
