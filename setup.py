from setuptools import setup

setup(
    name='pylenium',
    version='1.0.0',
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
    install_requires=['selenium', 'pytest', 'pytest-xdist'],
    data_files=[('../', ['pylenium/conftest.py', 'pylenium/pylenium.json'])]
)
