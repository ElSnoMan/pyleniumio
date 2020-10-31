from setuptools import setup, find_packages
import pylenium as app
import subprocess
import json


def get_list_of_packages() -> list:
    """ Get a list of current dependencies from pip via the cmd line """
    output = subprocess.getoutput("pip list --not-required --format=json")
    packages = []
    not_needed = ['setuptools', 'pip']
    for item in json.loads(output.split('\n')[0]):
        if item['name'] not in not_needed:
            packages.append(item['name'])

    return packages


setup(
    name='pyleniumio',
    version=app.__version__,
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/ElSnoMan/pyleniumio',
    license='MIT',
    author='Carlos Kidman',
    author_email='carlos@qap.dev',
    description='The best of Selenium and Cypress in a single Python Package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=get_list_of_packages(),
    data_files=[('', [
        'pylenium/scripts/pylenium.json',
        'pylenium/scripts/pytest.ini',
        'pylenium/scripts/drag_and_drop.js',
        'pylenium/scripts/load_jquery.js'
    ])],
    entry_points='''
        [console_scripts]
        pylenium=pylenium.scripts.cli:cli
    '''
)
