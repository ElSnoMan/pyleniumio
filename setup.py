from setuptools import setup, find_packages
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
    install_requires=[
        'selenium',
        'pytest',
        'pytest-xdist',
        'pytest-parallel',
        'pydantic',
        'pytest-reportportal',
        'Faker',
        'requests',
        'webdriver-manager',
        'click',
        'pyfiglet',
        'axe-selenium-python',
    ],
    data_files=[
        (
            '',
            [
                'pylenium/scripts/pylenium.json',
                'pylenium/scripts/pytest.ini',
                'pylenium/scripts/drag_and_drop.js',
                'pylenium/scripts/load_jquery.js',
            ],
        )
    ],
    entry_points='''
        [console_scripts]
        pylenium=pylenium.scripts.cli:cli
    ''',
)
