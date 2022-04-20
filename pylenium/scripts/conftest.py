"""
`conftest.py` and `pylenium.json` files should stay at your Workspace Root.

conftest.py
    Although this file is editable, you should only change its contents if you know what you are doing.
    Instead, you can create your own conftest.py file in the folder where you store your tests.

pylenium.json
    You can change the values, but DO NOT touch the keys or you will break the schema.

py
    The only fixture you really need from this is `py`. This is the instance of Pylenium for each test.
    Just pass py into your test and you're ready to go!

Examples:
    def test_go_to_google(py):
        py.visit('https://google.com')
        assert 'Google' in py.title()
"""

import copy
import json
import logging
import shutil
import sys
from pathlib import Path

import pytest
import requests
from faker import Faker
from pylenium.a11y import PyleniumAxe
from pylenium.config import PyleniumConfig, TestCase
from pylenium.driver import Pylenium
from reportportal_client import RPLogger, RPLogHandler


@pytest.fixture(scope="function")
def fake() -> Faker:
    """A basic instance of Faker to make test data."""
    return Faker()


@pytest.fixture(scope="function")
def api():
    """A basic instance of Requests to make HTTP API calls."""
    return requests


@pytest.fixture(scope="session")
def rp_logger(request):
    """Report Portal Logger"""
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    # Create handler for Report Portal if the service has been
    # configured and started.
    if hasattr(request.node.config, "py_test_service"):
        # Import Report Portal logger and handler to the test module.
        logging.setLoggerClass(RPLogger)
        rp_handler = RPLogHandler(request.node.config.py_test_service)
        # Add additional handlers if it is necessary
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        logger.addHandler(console_handler)
    else:
        rp_handler = logging.StreamHandler(sys.stdout)
    # Set INFO level for Report Portal handler.
    rp_handler.setLevel(logging.INFO)
    return logger


@pytest.fixture(scope="session", autouse=True)
def project_root() -> Path:
    """The Project (or Workspace) root as a filepath.

    * This conftest.py file should be in the Project Root if not already.
    """
    return Path(__file__).absolute().parent


@pytest.fixture(scope="session", autouse=True)
def test_run(project_root: Path, request) -> Path:
    """Creates the `/test_results` directory to store the results of the Test Run.

    Returns:
        The `/test_results` directory as a filepath (str).
    """
    session = request.node
    test_results_dir = project_root.joinpath("test_results")

    if test_results_dir.exists():
        # delete /test_results from previous Test Run
        shutil.rmtree(test_results_dir, ignore_errors=True)

    try:
        # race condition can occur between checking file existence and
        # creating the file when using pytest with multiple workers
        test_results_dir.mkdir(parents=True, exist_ok=True)
    except FileExistsError:
        pass

    for test in session.items:
        try:
            # make the test_result directory for each test
            test_results_dir.joinpath(test.name).mkdir(parents=True, exist_ok=True)
        except FileExistsError:
            pass

    return test_results_dir


@pytest.fixture(scope="session")
def _py_config(project_root, request) -> PyleniumConfig:
    """Read the PyleniumConfig for the test session

    1. This starts by deserializing the user-created pylenium.json from the Project Root.
    2. If that file is not found, then proceed with Pylenium Defaults.
    3. Then any CLI arguments override their respective key/values.
    """
    try:
        # 1. Load pylenium.json in Project Root, if available
        with project_root.joinpath("pylenium.json").open() as file:
            _json = json.load(file)
        config = PyleniumConfig(**_json)
    except FileNotFoundError:
        # 2. pylenium.json not found, proceed with defaults
        config = PyleniumConfig()

    # 3. Override with any CLI args/options
    # Driver Settings
    cli_remote_url = request.config.getoption("--remote_url")
    if cli_remote_url:
        config.driver.remote_url = cli_remote_url

    cli_browser_options = request.config.getoption("--options")
    if cli_browser_options:
        config.driver.options = [option.strip() for option in cli_browser_options.split(",")]

    cli_browser = request.config.getoption("--browser")
    if cli_browser:
        config.driver.browser = cli_browser

    cli_capabilities = request.config.getoption("--caps")
    if cli_capabilities:
        # --caps must be in '{"name": "value", "boolean": true}' format
        # with double quotes around each key. booleans are lowercase.
        config.driver.capabilities = json.loads(cli_capabilities)

    cli_wire_options = request.config.getoption("--wire_options")
    if cli_wire_options:
        # --wire_options must be in '{"name": "value", "boolean": true}' format
        # with double quotes around each key. booleans are lowercase.
        config.driver.seleniumwire_options = json.loads(cli_wire_options)

    cli_page_wait_time = request.config.getoption("--page_load_wait_time")
    if cli_page_wait_time and cli_page_wait_time.isdigit():
        config.driver.page_load_wait_time = int(cli_page_wait_time)

    # Logging Settings
    cli_screenshots_on = request.config.getoption("--screenshots_on")
    if cli_screenshots_on:
        shots_on = True if cli_screenshots_on.lower() == "true" else False
        config.logging.screenshots_on = shots_on

    cli_extensions = request.config.getoption("--extensions")
    if cli_extensions:
        config.driver.extension_paths = [ext.strip() for ext in cli_extensions.split(",")]

    return config


@pytest.fixture(scope="function")
def py_config(_py_config) -> PyleniumConfig:
    """Get a fresh copy of the PyleniumConfig for each test

    See _py_config for how the initial configuration is read.
    """
    return copy.deepcopy(_py_config)


@pytest.fixture(scope="function")
def test_case(test_run: Path, py_config, request) -> TestCase:
    """Manages data pertaining to the currently running Test Function or Case.

        * Creates the test-specific logger.

    Args:
        test_run: The Test Run (or Session) this test is connected to.

    Returns:
        An instance of TestCase.
    """
    test_name = request.node.name
    test_result_path = test_run.joinpath(test_name)
    py_config.driver.capabilities.update({"name": test_name})
    return TestCase(name=test_name, file_path=test_result_path)


@pytest.fixture(scope="function")
def py(test_case: TestCase, py_config, request, rp_logger):
    """Initialize a Pylenium driver for each test.

    Pass in this `py` fixture into the test function.

    Examples:
        def test_go_to_google(py):
            py.visit('https://google.com')
            assert 'Google' in py.title()
    """
    py = Pylenium(py_config)
    yield py
    try:
        if request.node.report.failed:
            # if the test failed, execute code in this block
            if py_config.logging.screenshots_on:
                screenshot = py.screenshot(str(test_case.file_path.joinpath("test_failed.png")))
                with open(screenshot, "rb") as image_file:
                    rp_logger.info(
                        "Test Failed - Attaching Screenshot",
                        attachment={"name": "test_failed.png", "data": image_file, "mime": "image/png"},
                    )
    except AttributeError:
        rp_logger.error("Unable to access request.node.report.failed, unable to take screenshot.")
    except TypeError:
        rp_logger.info("Report Portal is not connected to this test run.")
    py.quit()


@pytest.fixture(scope="function")
def axe(py) -> PyleniumAxe:
    """The aXe A11y audit tool as a fixture."""
    return PyleniumAxe(py.webdriver)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Yield each test's outcome so we can handle it in other fixtures."""
    outcome = yield
    report = outcome.get_result()
    if report.when == "call":
        setattr(item, "report", report)
    return report


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="", help="The lowercase browser name: chrome | firefox")
    parser.addoption("--remote_url", action="store", default="", help="Grid URL to connect tests to.")
    parser.addoption("--screenshots_on", action="store", default="", help="Should screenshots be saved? true | false")
    parser.addoption("--pylog_level", action="store", default="", help="Set the pylog_level: 'off' | 'info' | 'debug'")
    parser.addoption(
        "--options",
        action="store",
        default="",
        help='Comma-separated list of Browser Options. Ex. "headless, incognito"',
    )
    parser.addoption(
        "--caps",
        action="store",
        default="",
        help='List of key-value pairs. Ex. \'{"name": "value", "boolean": true}\'',
    )
    parser.addoption(
        "--page_load_wait_time",
        action="store",
        default="",
        help="The amount of time to wait for a page load before raising an error. Default is 0.",
    )
    parser.addoption(
        "--extensions", action="store", default="", help='Comma-separated list of extension paths. Ex. "*.crx, *.crx"'
    )
    parser.addoption(
        "--wire_options",
        action="store",
        default="",
        help='Dict of key-value pairs as a string. Ex. \'{"name": "value", "boolean": true}\'',
    )
