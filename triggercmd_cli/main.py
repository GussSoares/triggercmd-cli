import typer
from pyfiglet import Figlet
from rich.console import Console

from triggercmd_cli import __version__
from triggercmd_cli.command.command import command_app as app

# app = typer.Typer(help=__doc__)
console = Console()
app.help = __doc__
# app.add_typer(command_app, name="command")


def get_version(version: bool):
    if version:
        typer.echo(
            f"\n{Figlet(font='slant').renderText('TriggerCMD CLI')}\n"
            f"\nTriggerCMD CLI Version: {__version__}\n"
        )
        raise typer.Exit()
    else:
        typer.echo(f"\n{Figlet(font='slant').renderText('TriggerCMD CLI')}")


@app.callback()
def main(
    version: bool = typer.Option(
        None,
        "--version",
        "-v",
        callback=get_version,
        is_eager=True,
        help="Display TriggerCMD CLI version.",
    )
):
    return


def run():
    try:
        app()
    except Exception as e:
        console.print(f"[red]Error:[/] {e}")


if __name__ == "__main__":
    run()
