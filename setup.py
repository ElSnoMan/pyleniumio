from os import path
from setuptools import setup, find_packages


this_directory = path.abspath(path.dirname(__file__))
with open(f'{this_directory}/docs/README.md', 'r') as f:
    long_description = f.read()


setup(
    name='pyleniumio',
    version='1.9.3',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/ElSnoMan/pyleniumio',
    license='MIT',
    author='Carlos Kidman',
    author_email='carlos@qap.dev',
    description='The best of Selenium and Cypress in a single Python Package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
        'selenium', 'pytest', 'pytest-xdist', 'pytest-parallel', 'pydantic', 'pytest-reportportal',
        'faker', 'requests', 'webdriver-manager', 'click', 'pyfiglet'
    ],
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
