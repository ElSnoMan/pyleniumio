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
from pylenium import Pylenium
from pylenium.config import PyleniumConfig, TestCase
from pylenium.logging import Logger


@pytest.fixture(scope='session')
def test_context_filepath() -> str:
    """ The filepath from the context you executed the tests from.

    * If you run the test(s) from the CLI from your actual Workspace Root, then your context will be the Workspace Root.

    * If you run the test(s) with the `Play` button in the UI, the context is the directory where that file lives.

    Returns:
        The Test Run's context (aka directory) as a filepath (str).
    """
    return os.path.dirname(os.path.abspath(__file__))


@pytest.fixture(scope='session')
def test_run(test_context_filepath) -> str:
    """ Creates the `/test_results` directory to store the results of the Test Run.

    Args:
        test_context_filepath: It will base the filepath from the fixture.

    Returns:
        The `/test_results` directory as a filepath (str).
    """
    test_results_dir = f'{test_context_filepath}/test_results'

    if os.path.exists(test_results_dir):
        # delete /test_results from previous Test Run
        shutil.rmtree(test_results_dir)
    if not os.path.exists(test_results_dir):
        # create /test_results for this Test Run
        os.mkdir(test_results_dir)
    return test_results_dir


@pytest.fixture(scope='function')
def test_case(test_run, request) -> TestCase:
    """ Manages data pertaining to the currently running Test Function or Case.

    * Creates the `/{test_name}` directory to store the artifacts of the Test Function or Case.
    * Creates the test-specific logger.

    Args:
        test_run: It will base the filepath from the fixture.

    Returns:
        dict with  `/{test_name}` directory as a filepath (str).
    """
    test_name = request.node.name
    test_result_path = f'{test_run}/{test_name}'

    if not os.path.exists(test_result_path):
        os.mkdir(test_result_path)

    logger = Logger(test_name, test_result_path)

    test = {
        'name': test_name,
        'file_path': test_result_path,
        'logger': logger
    }
    return TestCase(**test)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """ Yield each test's outcome so we can handle it in other fixtures. """
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture('function')
def py_config(test_context_filepath) -> PyleniumConfig:
    """ Initialize a PyleniumConfig for each test using pylenium.json """
    with open(f'{test_context_filepath}/pylenium.json') as file:
        _json = json.load(file)
    return PyleniumConfig(**_json)


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
        py.screenshot(f'{test_case.file_path}/test_failed.png')
    py.quit()


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
