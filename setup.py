from setuptools import setup, find_packages


setup(
    name='pyleniumio',
    version='1.9.4',
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
