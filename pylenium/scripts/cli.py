""" The Pylenium CLI.

We are using `click` to create the CLI interface.
In short, the structure of the interface looks like this:

@click.group() as cli         # this is then publicly exposed as `pylenium` in the user's terminal
    @cli.command()            # A
    @cli.command()            # B

    @cli.group() as portal
        @portal.command()     # C
        @portal.command()     # D

This structure is what gives us commands and sub-commands.
Examples:
    # Use command A
    $ pylenium init

    # Use portal command C
    $ pylenium portal download

For more information, visit their official docs: https://click.palletsprojects.com/en/7.x/
"""

import os
import shutil

import click
from pyfiglet import Figlet

from pylenium.scripts import report_portal


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
@click.version_option()
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
        _copy(file=pytest_ini, to_dir=user_cwd, message='pytest.ini was created at:')


@cli.command()
def joy():
    custom_fig = Figlet(font='colossal')
    click.echo(custom_fig.renderText('Pyl e n i u m Sparks Joy'))


# REPORT PORTAL #
#################

@cli.group()
def portal():
    """ CLI Commands to work with ReportPortal.io """
    pass


@portal.command()
def download():
    """ Download the ReportPortal docker-compose.yml file as docker-compose.report-portal.yml """
    report_portal.download_compose_yaml_file()
    click.echo('[SUCCESS] docker-compose.report-portal.yml file created!')
    click.echo('Depending on your OS, you will want to configure this file and your machine.')
    click.echo('Use the ReportPortal docs to see how you should configure your environment and .yml file:')
    click.echo('''
        ReportPortal Deploy with Docker
            https://reportportal.io/docs/Deploy-with-Docker
    ''')
    click.echo('Once configured, just use `$ pylenium portal up` to spin up your instance of ReportPortal!')


@portal.command()
def up():
    """ Spin up the ReportPortal instance using docker-compose.report-portal.yml """
    report_portal.compose_up()
    click.echo('[SUCCESS] ReportPortal instance created!')
    click.echo('1. Open the portal by going to: http://localhost:8080')
    click.echo('2. Login using the Admin or User credentials:')
    click.echo('''
        Admin
            username: superadmin
            password: erebus
        User
            username: default
            password: 1q2w3e
    ''')
    click.echo("* Make sure to change your password once you've logged in!")
    click.echo('3. Copy the ACCESS TOKEN, in User Profile, and paste it in the UUID variable in pytest.ini')
    click.echo('''
        All set! Now run your tests using `--reportportal`. For more info on the pytest plugin, visit:
            https://github.com/reportportal/agent-python-pytest
    ''')


@portal.command()
def down():
    """ Tear down the ReportPortal instance. """
    report_portal.down()
    click.echo('[SUCCESS] ReportPortal instance removed!')


if __name__ == '__main__':
    cli()
