import os
import shutil

import click
from pyfiglet import Figlet

from pylenium.scripts import report_portal

VERSION = '1.8.4'


def _copy(file, to_dir, message) -> str:
    """ Copies a file to the given directory.

    If the file exists, it is overwritten.

    Returns:
        The absolute path of the newly copied file.
    """
    newly_created_path = shutil.copy(src=file, dst=to_dir)
    click.echo(f'{message} {newly_created_path}')
    return newly_created_path


@click.group()
def cli():
    """ The Pylenium CLI. """
    pass


@cli.command()
@click.option('-c', '--overwrite-conftest', type=bool, show_default=True, is_flag=True)
@click.option('-p', '--overwrite-pylenium-json', type=bool, show_default=True, is_flag=True)
@click.option('-i', '--overwrite-pytest-ini', type=bool, show_default=True, is_flag=True)
def init(overwrite_conftest, overwrite_pylenium_json, overwrite_pytest_ini):
    """ Initializes Pylenium into the current directory.

    By default, this creates (if they do not exist):
    * conftest.py
    * pylenium.json
    * pytest.ini

    If you want to overwrite these existing files, use the available Options.
    """
    scripts_path = os.path.dirname(os.path.abspath(__file__))
    user_cwd = os.getcwd()

    conftest = f'{scripts_path}/conftest.py'
    pylenium_json = f'{scripts_path}/pylenium.json'
    pytest_ini = f'{scripts_path}/pytest.ini'

    # initialize conftest.py
    if os.path.exists(f'{user_cwd}/conftest.py'):
        if overwrite_conftest:
            _copy(file=conftest, to_dir=user_cwd, message='conftest.py was overwritten at:')
        else:
            click.echo('conftest.py already exists at this location. '
                       'Use -c flag if you want to replace it with the latest.')
    else:
        _copy(file=conftest, to_dir=user_cwd, message='conftest.py was created at:')

    # initialize pylenium.json
    if os.path.exists(f'{user_cwd}/pylenium.json'):
        if overwrite_pylenium_json:
            _copy(file=pylenium_json, to_dir=user_cwd, message='pylenium.json was overwritten at:')
        else:
            click.echo('pylenium.json already exists at this location. '
                       'Use -p flag if you want to replace it with the latest defaults.')
    else:
        _copy(file=pylenium_json, to_dir=user_cwd, message='pylenium.json was created at:')

    # initialize pytest.ini
    if os.path.exists(f'{user_cwd}/pytest.ini'):
        if overwrite_pytest_ini:
            _copy(file=pytest_ini, to_dir=user_cwd, message='pytest.ini was overwritten at:')
        else:
            click.echo('pytest.ini already exists at this location. '
                       'Use -i flag if you want to replace it with the latest defaults.')
    else:
        _copy(file=pytest_ini, to_dir=pytest_ini, message='pytest.ini was created at:')


@cli.command()
def portal():
    # 1. Download the ReportPortal `docker-compose.yml` file as "docker-compose.report-portal.yml"
    report_portal.download_compose_yaml_file()

    # 2. Setup permissions for ElasticSearch
    report_portal.setup_elastic_search_permissions()

    # 3. Configure the YAML file based on OS

    # 4. docker-compose up
    report_portal.compose_up()

    # 5. Display info on newly created instance like the URL to open in a browser


@cli.command()
def version():
    """ Displays the current version of Pylenium. """
    click.echo(VERSION)


@cli.command()
def joy():
    custom_fig = Figlet(font='colossal')
    click.echo(custom_fig.renderText('Pyl e n i u m Sparks Joy'))


if __name__ == '__main__':
    cli()
