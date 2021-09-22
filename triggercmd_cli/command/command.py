"""
TriggerCMD CLI

Linux CLI client to TriggerCMD cloud service agent.

You probably want to install completion for the typer command.
If you are using bash, try to type:

$ triggercmd --install-completion bash

https://github.com/GussSoares/triggercmd-cli
"""

import time

import typer
from rich.console import Console
from rich.table import Table

from triggercmd_cli.command.entities import Command
from triggercmd_cli.command.wizard import CommandWizard
from triggercmd_cli.utils import functions

command_app = typer.Typer(help=__doc__)
console = Console()


@command_app.command(help="Create a new command.")
def new():
    console.rule("Create a command")

    new = CommandWizard.new()

    with console.status("[yellow]Please wait...[/]"):
        time.sleep(5)
        Command.new(**new)

    message = f"\n[green]Success![/] Command `{new['trigger']}` created."
    console.print(message)
    console.rule()


@command_app.command(help="Edit a command existent.")
def edit():
    console.rule("Edit a command")

    commands = functions.get_command_titles()
    command_selected = CommandWizard.select_command(commands)
    edited = CommandWizard.edit(command_selected)

    with console.status("[yellow]Please wait...[/]"):
        time.sleep(5)
        Command.edit(command_selected["trigger"], edited)

    message = f"\n[green]Success![/] Command `{edited['trigger']}` edited."
    console.print(message)
    console.rule()


@command_app.command(help="Remove a command existent.")
def remove():
    console.rule("Remove a command")

    commands = functions.get_command_titles()
    selected = CommandWizard.select_command(commands)
    message = f"\n[green]Success![/] Command `{selected['trigger']}` removed."

    if CommandWizard.confirm("Are you sure you want remove this command?"):

        with console.status("[yellow]Please wait...[/]"):
            time.sleep(5)
            Command.remove(selected)

        console.print(message)
        console.rule()


@command_app.command(help="List all commands.")
def list():

    data = functions.load_json_file()

    table = Table(title="Command List", title_justify="center")
    table.add_column("Trigger")
    table.add_column("Command")
    table.add_column("Ground")
    table.add_column("Voice")
    table.add_column("Allow Params")

    for row in data:
        table.add_row(
            row.get("trigger"),
            row.get("command"),
            row.get("ground"),
            row.get("voice"),
            row.get("allowParams"),
        )

    console.print()
    console.rule("TriggerCMD")
    console.print(table)
    console.rule("")


@command_app.command(help="Test a commands.")
def test(trigger: str = typer.Option("", help="Trigger name")):
    console.rule("Test a command")

    if not trigger:
        commands = functions.get_command_titles()
        trigger = CommandWizard.select_command(commands).get("trigger")

    response, status = Command.test("lenovo", trigger)

    if status == 200:
        message = f"[green]Success[/] {response.get('message')}"
    else:
        message = f"[red]Error[/] {response.get('error').get('response')}"

    console.print(message)
    console.rule()
