""" The Pylenium CLI using Typer.

For more information, visit their official docs: https://typer.tiangolo.com/
"""

import os
import shutil

import typer

from pylenium.scripts import allure_reporting as allure_

app = typer.Typer()
app.add_typer(allure_.app, name="allure", help="Allure Reporting Commands")


def _copy(file, to_dir, message) -> str:
    """Copies a file to the given directory.

    If the file exists, it is overwritten.

    Returns:
        The absolute path of the newly copied file.
    """
    newly_created_path = shutil.copy(src=file, dst=to_dir)
    typer.secho(f"✅ {message} {newly_created_path}", fg=typer.colors.BRIGHT_GREEN)
    return newly_created_path


@app.command()
def init(
    overwrite_conftest: bool = typer.Option(False, "--conftest", "-c", help="Overwrite conftest.py"),
    overwrite_pylenium_json: bool = typer.Option(False, "--pylenium_json", "-p", help="Overwrite pylenium.json"),
    overwrite_pytest_ini: bool = typer.Option(False, "--pytest_ini", "-i", help="Overwrite pytest.ini"),
):
    """Initializes Pylenium into the current directory.

    By default, this creates (if they do not exist): conftest.py, pylenium.json, pytest.ini

    If you want to overwrite these existing files, use the available Options.
    """
    scripts_path = os.path.dirname(os.path.abspath(__file__))
    user_cwd = os.getcwd()

    conftest = f"{scripts_path}/conftest.py"
    pylenium_json = f"{scripts_path}/pylenium.json"
    pytest_ini = f"{scripts_path}/pytest.ini"

    # initialize conftest.py
    if os.path.exists(f"{user_cwd}/conftest.py"):
        if overwrite_conftest:
            _copy(file=conftest, to_dir=user_cwd, message="conftest.py was overwritten at:")
        else:
            typer.secho("conftest.py already exists at this location", fg=typer.colors.BRIGHT_YELLOW)
            typer.secho("💡 Use -c flag if you want to replace it with the latest\n", fg=typer.colors.BRIGHT_CYAN)
    else:
        _copy(file=conftest, to_dir=user_cwd, message="conftest.py was created at:")

    # initialize pylenium.json
    if os.path.exists(f"{user_cwd}/pylenium.json"):
        if overwrite_pylenium_json:
            _copy(file=pylenium_json, to_dir=user_cwd, message="pylenium.json was overwritten at:")
        else:
            typer.secho("pylenium.json already exists at this location", fg=typer.colors.BRIGHT_YELLOW)
            typer.secho("💡 Use -p flag if you want to replace it with the latest defaults\n", fg=typer.colors.BRIGHT_CYAN)
    else:
        _copy(file=pylenium_json, to_dir=user_cwd, message="pylenium.json was created at:")

    # initialize pytest.ini
    if os.path.exists(f"{user_cwd}/pytest.ini"):
        if overwrite_pytest_ini:
            _copy(file=pytest_ini, to_dir=user_cwd, message="pytest.ini was overwritten at:")
        else:
            typer.secho("pytest.ini already exists at this location", fg=typer.colors.BRIGHT_YELLOW)
            typer.secho("💡 Use -i flag if you want to replace it with the latest defaults\n", fg=typer.colors.BRIGHT_CYAN)
    else:
        _copy(file=pytest_ini, to_dir=user_cwd, message="pytest.ini was created at:")


if __name__ == "__main__":
    app()
