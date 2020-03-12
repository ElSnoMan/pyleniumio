from setuptools import setup

setup(
    name='pylenium',
    version='0.1.0',
    packages=['pylenium'],
    package_dir={'pylenium': 'pylenium'},
    package_data={'': [
        'conftest.py', 'pylenium.json'
    ]},
    url='https://github.com/ElSnoMan/pyleniumio',
    license='MIT',
    author='Carlos Kidman',
    author_email='carlos@qap.dev',
    description='Cypress-like Selenium bindings',
    long_description=open('README.md').read(),
    install_requires=['selenium', 'pytest', 'pytest-xdist']
)
