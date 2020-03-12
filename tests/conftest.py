import pytest
from pylenium import Pylenium


@pytest.fixture(scope='function')
def py():
    """ Default Fixture. """
    py = Pylenium()
    yield py
    py.quit()


@pytest.fixture(scope='session')
def py_factory():
    """ Pylenium Fixture as a Factory. """
    def _pylenium(wait_time=10):
        py = Pylenium(wait_time)
        return py
    return _pylenium


@pytest.fixture(scope='module')
def driver(py_factory):
    """ This Project's integration testing fixture. """
    py = py_factory()
    py.visit('https://deckshop.pro')
    yield py
    py.quit()
