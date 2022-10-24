""" Allure reporting integration """

from typing import List
import rich_click as click
from pylenium.scripts.cli_utils import run_process, parse_response


def _install(commands: List[str]):
    """Command to install allure via the CLI"""
    click.echo("\n🛑 It's recommended that you run the above command(s) yourself to see all the output 🛑")
    answer = click.prompt("\nWould you like to proceed? (y/n)", default="n")
    try:
        if answer == "y":
            response = run_process(commands)
            _, err = parse_response(response)
            if response.returncode != 0:
                click.echo(f"😢 Unable to install allure. {err}")
                click.echo("Visit allure's docs for more options: https://docs.qameta.io/allure/#_get_started")
                return
            click.echo("✅ allure installed. Try running `pylenium allure check` to verify the installation.")
            return

        if answer == "n" or answer is not None:
            click.echo("❌ Command aborted")
            return
    except FileNotFoundError:
        click.echo("One of the commands was not found...")
        click.echo("Visit their docs for more info: https://docs.qameta.io/allure/#_get_started")


def install_for_linux():
    """Install allure on a Debian-based Linux machine."""
    click.echo("This command only works for Debian-based Linux and uses sudo:\n")
    click.echo("    sudo apt-add-repository ppa:qameta/allure")
    click.echo("    sudo apt-get update")
    click.echo("    sudo apt-get install allure")
    _install([
            "sudo", "apt-add-repository", "ppa:qameta/allure", "-y",
            "sudo", "apt-get", "update", "-y",
            "sudo", "apt-get", "install", "allure", "-y",
        ])


def install_for_mac():
    click.echo("This command uses homebrew to do the installation:\n")
    click.echo("    brew install allure")
    _install(["brew", "install", "allure"])


def install_for_windows():
    click.echo("This command uses scoop to do the installation:\n")
    click.echo("    scoop install allure")
    _install(["scoop", "install", "allure"])
