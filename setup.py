from setuptools import setup, find_packages
from pylenium.scripts.setup_tools import get_install_requirements
import pylenium as app


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
    install_requires=get_install_requirements('Pipfile'),
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
