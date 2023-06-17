""" Allure reporting integration """
import platform
from typing import List

import typer

from pylenium.scripts.cli_utils import parse_response, run_process


def _install(commands: List[str]):
    """Command to install allure via the CLI"""
    typer.secho("\n🛑 It's recommended that you run the above command(s) yourself to see all the output 🛑", fg=typer.colors.BRIGHT_YELLOW)
    answer = typer.prompt("\nWould you like to proceed? (y/n)", default="n")
    try:
        if answer == "y":
            response = run_process(commands)
            _, err = parse_response(response)
            if response.returncode != 0:
                typer.secho(f"😢 Unable to install allure. {err}", fg=typer.colors.BRIGHT_RED)
                typer.secho("Visit allure's docs for more options: https://docs.qameta.io/allure/#_get_started", fg=typer.colors.BRIGHT_CYAN)
                return
            typer.secho("✅ allure installed. Try running `pylenium allure check` to verify the installation.", fg=typer.colors.BRIGHT_GREEN)
            return

        if answer == "n" or answer is not None:
            typer.secho("❌ Command aborted")
            return
    except FileNotFoundError:
        typer.secho("One of the commands was not found...", fg=typer.colors.BRIGHT_RED)
        typer.secho("Visit their docs for more info: https://docs.qameta.io/allure/#_get_started", fg=typer.colors.BRIGHT_CYAN)


def install_for_linux():
    """Install allure on a Debian-based Linux machine."""
    typer.secho("This command only works for Debian-based Linux and uses sudo:\n", fg=typer.colors.BRIGHT_YELLOW)
    typer.secho("    sudo apt-add-repository ppa:qameta/allure")
    typer.secho("    sudo apt-get update")
    typer.secho("    sudo apt-get install allure")
    _install(
        [
            "sudo",
            "apt-add-repository",
            "ppa:qameta/allure",
            "-y",
            "sudo",
            "apt-get",
            "update",
            "-y",
            "sudo",
            "apt-get",
            "install",
            "allure",
            "-y",
        ]
    )


def install_for_mac():
    typer.secho("This command uses homebrew to do the installation:\n", fg=typer.colors.BRIGHT_YELLOW)
    typer.secho("    brew install allure")
    _install(["brew", "install", "allure"])


def install_for_windows():
    typer.secho("This command uses scoop to do the installation:\n", fg=typer.colors.BRIGHT_YELLOW)
    typer.secho("    scoop install allure")
    _install(["scoop", "install", "allure"])


app = typer.Typer()


@app.command()
def check():
    """Check if the allure CLI is installed on the current machine."""
    typer.secho("\n$ allure --version")
    err_message = "\n❌ allure is not installed or not added to the PATH. Visit https://docs.qameta.io/allure/#_get_started"
    try:
        response = run_process(["allure", "--version"])
        out, err = parse_response(response)
        if response.returncode != 0:
            typer.secho(err_message, fg=typer.colors.BRIGHT_RED)
            typer.secho(err, fg=typer.colors.BRIGHT_RED)
            return
        typer.secho(f"\n✅ allure is installed with version: {out}", fg=typer.colors.BRIGHT_GREEN)
    except FileNotFoundError:
        typer.secho(err_message)


@app.command()
def install():
    """Install the allure CLI to the current machine."""
    typer.secho(
        "\n💡 For more installation options and details, please visit allure's docs: https://docs.qameta.io/allure/#_get_started", fg=typer.colors.BRIGHT_CYAN
    )
    operating_system = platform.system()
    if operating_system.upper() == "LINUX":
        install_for_linux()
        return

    if operating_system.upper() == "DARWIN":
        install_for_mac()
        return

    if operating_system.upper() == "WINDOWS":
        install_for_windows()
        return


@app.command()
def serve(folder: str = typer.Option("allure-report", "--folder", "-f", help="The folder path to the allure report")):
    """Start the allure server and serve the allure report given its folder path."""
    typer.secho(f"\n$ allure serve {folder}")
    typer.secho("Press <Ctrl+C> to exit", fg=typer.colors.BRIGHT_CYAN)
    try:
        response = run_process(["allure", "serve", folder])
        _, err = parse_response(response)
        if response.returncode != 0:
            typer.secho(f"\n❌ Unable to serve allure report. Check that the folder path is valid. {err}", fg=typer.colors.BRIGHT_RED)
    except FileNotFoundError:
        typer.secho("\n❌ allure is not installed or not added to the PATH. Visit https://docs.qameta.io/allure/#_get_started", fg=typer.colors.BRIGHT_RED)


if __name__ == "__main__":
    app()
