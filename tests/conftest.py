import json
import pytest
from pylenium import Pylenium
from pylenium.config import PyleniumConfig


@pytest.fixture
def py_config():
    """ Setup PyleniumConfig. """
    with open('../pylenium/config/pylenium.json') as file:
        _json = json.load(file)
    return PyleniumConfig(**_json)


@pytest.fixture(scope='function')
def py(py_config):
    """ Default Fixture. """
    py = Pylenium()
    yield py
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
    with open('../pylenium/config/pylenium.json') as file:
        _json = json.load(file)
    config =  PyleniumConfig(**_json)

    # init driver
    py = py_factory(config)
    py.visit('https://deckshop.pro')
    yield py
    py.quit()
