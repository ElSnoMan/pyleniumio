"""
`conftest.py` and `pylenium.json` files should stay at your Workspace Root.

conftest.py
    Although this file is editable, you should only change its contents if you know what you are doing.
    Instead, you can create your own conftest.py file win the folder where you store your tests.

pylenium.json
    You can change the values, but DO NOT touch the keys or you will break the schema.

py
    The only fixture you really need from this is `py`. This is the instance of Pylenium for each test.
    Just pass py into your test and you're ready to go!

Examples:
    def test_go_to_google(py):
        py.visit('https://google.com')
        assert 'Google' in py.title
"""

import json
import os
import shutil

import pytest
import requests
from faker import Faker

from pylenium import Pylenium
from pylenium.config import PyleniumConfig, TestCase
from pylenium.logging import Logger


def make_dir(filepath) -> bool:
    """ Make a directory.

    Returns:
        True if successful, False if not.
    """
    try:
        os.mkdir(filepath)
        return True
    except FileExistsError:
        return False


@pytest.fixture(scope='function')
def fake() -> Faker:
    """ A basic instance of Faker to make test data."""
    return Faker()


@pytest.fixture(scope='function')
def api():
    """ A basic instance of Requests to make HTTP API calls. """
    return requests


@pytest.fixture(scope='session', autouse=True)
def project_root() -> str:
    """ The Project (or Workspace) root as a filepath.

    * This conftest.py file should be in the Project Root if not already.
    """
    return os.path.dirname(os.path.abspath(__file__))


@pytest.fixture(scope='session', autouse=True)
def test_run(project_root, request) -> str:
    """ Creates the `/test_results` directory to store the results of the Test Run.

    Returns:
        The `/test_results` directory as a filepath (str).
    """
    session = request.node
    test_results_dir = f'{project_root}/test_results'

    if os.path.exists(test_results_dir):
        # delete /test_results from previous Test Run
        shutil.rmtree(test_results_dir, ignore_errors=True)
    if not os.path.exists(test_results_dir):
        # create /test_results for this Test Run
        make_dir(test_results_dir)

    for test in session.items:
        # make the test_result directory for each test
        make_dir(f'{test_results_dir}/{test.name}')

    return test_results_dir


@pytest.fixture('function')
def py_config(project_root, request) -> PyleniumConfig:
    """ Initialize a PyleniumConfig for each test

    This starts by deserializing pylenium.json into PyleniumConfig.
    Then any CLI arguments override their respective key/values.
    """
    # Deserialize pylenium.json
    try:
        with open(f'{project_root}/pylenium.json') as file:
            _json = json.load(file)
        config = PyleniumConfig(**_json)
    except BaseException:
        raise FileNotFoundError("Could not find pylenium.json in Project Root."
                                " Make sure Pylenium's pylenium.json and conftest.py are at the top-level directory.")

    # Override with any CLI args/options
    # Driver Settings
    cli_remote_url = request.config.getoption('--remote_url')
    if cli_remote_url:
        config.driver.remote_url = cli_remote_url

    cli_browser_options = request.config.getoption('--options')
    if cli_browser_options:
        config.driver.options = [option.strip() for option in cli_browser_options.split(',')]

    # Logging Settings
    cli_pylog_level = request.config.getoption('--pylog_level')
    if cli_pylog_level:
        config.logging.pylog_level = cli_pylog_level

    cli_screenshots_on = request.config.getoption('--screenshots_on')
    if cli_screenshots_on:
        shots_on = True if cli_screenshots_on.lower() == 'true' else False
        config.logging.screenshots_on = shots_on

    return config


@pytest.fixture(scope='function')
def test_case(test_run, py_config, request) -> TestCase:
    """ Manages data pertaining to the currently running Test Function or Case.

        * Creates the test-specific logger.

    Args:
        test_run: The Test Run (or Session) this test is connected to.

    Returns:
        An instance of TestCase.
    """
    test_name = request.node.name
    test_result_path = f'{test_run}/{test_name}'
    logger = Logger(test_name, test_result_path, py_config.logging.pylog_level)

    test = {
        'name': test_name,
        'file_path': test_result_path,
        'logger': logger
    }
    return TestCase(**test)


@pytest.fixture(scope='function')
def py(test_case, py_config, request):
    """ Initialize a Pylenium driver for each test.

    Pass in this `py` fixture into the test function.

    Examples:
        def test_go_to_google(py):
            py.visit('https://google.com')
            assert 'Google' in py.title
    """
    py = Pylenium(py_config, test_case.logger)
    yield py
    if request.node.rep_call.failed:
        # if the test failed, execute code in this block
        if py_config.logging.screenshots_on:
            py.screenshot(f'{test_case.file_path}/test_failed.png')
    py.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """ Yield each test's outcome so we can handle it in other fixtures. """
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


def pytest_addoption(parser):
    parser.addoption(
        '--browser', action='store', default='', help='The lowercase browser name: chrome | firefox'
    )
    parser.addoption(
        '--remote_url', action='store', default='', help='Grid URL to connect tests to.'
    )
    parser.addoption(
        '--screenshots_on', action='store', default='', help="Should screenshots be saved? true | false"
    )
    parser.addoption(
        '--pylog_level', action='store', default='', help="Set the pylog_level: 'off' | 'info' | 'debug'"
    )
    parser.addoption(
        '--options', action='store',
        default='', help='Comma-separated list of Browser Options. Ex. "headless, incognito"'
    )


@pytest.fixture(scope='class')
def pyc(test_run, py_config, request):
    """ A singleton of Pylenium to be shared in the tests of a Class.

    The tests in the class are executed sequentially and in order.

    Warnings:
        This approach is NOT recommended. You should want your tests to be modular, atomic and deterministic.

    Examples:
          class TestGoogle:
              def test_visit_google(self, pyc):
                  # first test navigates to google.com
                  pyc.visit('https://google.com')

              def test_google_search(self, pyc):
                  # second test is already on google.com, test search
                  pyc.get("[name='q']").type('puppies', Keys.ENTER)
                  assert 'puppies' in pyc.title
    """
    # init logger
    class_name = request.node.name
    file_path = f'{test_run}/{class_name}'
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    logger = Logger(class_name, file_path)

    # init driver
    py = Pylenium(py_config, logger)
    yield py
    py.quit()
