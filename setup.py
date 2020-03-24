from setuptools import setup

setup(
    name='pyleniumio',
    version='1.2.9',
    packages=[
        'pylenium'
    ],
    package_dir={'pylenium': 'pylenium'},
    url='https://github.com/ElSnoMan/pyleniumio',
    license='MIT',
    author='Carlos Kidman',
    author_email='carlos@qap.dev',
    description='Cypress-like bindings for Selenium with Python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=['selenium', 'pytest', 'pytest-xdist', 'pydantic', 'faker', 'requests'],
    data_files=[('..', ['conftest.py', 'pylenium.json'])]
)
