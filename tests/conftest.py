import json
import os
import shutil

import pytest
from pylenium import Pylenium
from pylenium.config import PyleniumConfig


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


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """ Yield each test's outcome so we can handle it in other fixtures. """
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture
def py_config(test_context_filepath):
    """ Initialize a PyleniumConfig for each test using pylenium.json """
    with open(f'{test_context_filepath}/pylenium.json') as file:
        _json = json.load(file)
    return PyleniumConfig(**_json)


@pytest.fixture
def py(test_run, py_config, request):
    """ Initialize a Pylenium driver for each test.

    Pass in this `py` fixture into the test function.

    Examples:
        def test_go_to_google(py):
            py.visit('https://google.com')
            assert 'Google' in py.title
    """
    test_name = request.node.name
    test_result_path = f'{test_run}/{test_name}'

    if not os.path.exists(test_result_path):
        os.mkdir(test_result_path)

    py = Pylenium(py_config)
    yield py
    if request.node.rep_call.failed:
        # if the test failed, execute code in this block
        py.screenshot(f'{test_result_path}/test_failed.png')
    py.quit()


@pytest.fixture(scope='session')
def py_factory():
    """ Pylenium Fixture as a Factory. """
    def _pylenium(config: PyleniumConfig):
        py = Pylenium(config)
        return py
    return _pylenium


@pytest.fixture(scope='module')
def driver(py_factory):
    """ This Project's integration testing fixture. """
    # setup config
    with open('../pylenium/pylenium.json') as file:
        _json = json.load(file)
    config = PyleniumConfig(**_json)

    # init driver
    py = py_factory(config)
    py.visit('https://deckshop.pro')
    yield py
    py.quit()
