import os
import shutil
import click


def _copy(file, to_dir, message) -> str:
    newly_created_path = shutil.copy(src=file, dst=to_dir)
    click.echo(f'{message} {newly_created_path}')
    return newly_created_path


@click.group()
def cli():
    """ The Pylenium CLI. """
    pass


@cli.command()
@click.option('-c', '--overwrite-conftest', type=bool, default=False, show_default=True)
@click.option('-p', '--overwrite-pylenium-json', type=bool, default=False, show_default=True)
def init(overwrite_conftest, overwrite_pylenium_json):
    """ Initializes Pylenium into the current directory.

    * By default, this creates a conftest.py file and a pylenium.json config file if they do not exist.

    If you want to overwrite these existing files, use the available Options.
    """
    scripts_path = os.path.dirname(os.path.abspath(__file__))
    user_cwd = os.getcwd()

    conftest = f'{scripts_path}/conftest.py'
    pylenium_json = f'{scripts_path}/pylenium.json'

    # initialize conftest.py
    if os.path.exists(f'{user_cwd}/conftest.py'):
        if overwrite_conftest:
            _copy(file=conftest, to_dir=user_cwd, message='conftest.py was overwritten at:')
        else:
            click.echo('conftest.py already exists at this location. '
                       'Use -c=true if you want to replace it with the latest.')
    else:
        _copy(file=conftest, to_dir=user_cwd, message='conftest.py was created at:')

    # initialize pylenium.json
    if os.path.exists(f'{user_cwd}/pylenium.json'):
        if overwrite_pylenium_json:
            _copy(file=pylenium_json, to_dir=user_cwd, message='pylenium.json was overwritten at:')
        else:
            click.echo('pylenium.json already exists at this location. '
                       'Use -p=true if you want to replace it with the latest defaults.')
    else:
        _copy(file=pylenium_json, to_dir=user_cwd, message='pylenium.json was created at:')


@cli.command()
def version():
    """ Displays the current version of Pylenium. """
    click.echo('1.7.0')


if __name__ == '__main__':
    cli()
