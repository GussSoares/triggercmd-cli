import typer

from triggercmd_cli.command.command import command_app

app = typer.Typer(help=__doc__)

app.add_typer(command_app, name="command")


def run():
    app()
