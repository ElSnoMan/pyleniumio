import pytest
from pylenium.pydriver import Pylenium


@pytest.fixture
def py():
    driver = Pylenium()
    yield driver
    driver.quit()


@pytest.fixture(scope='module')
def driver():
    driver = Pylenium()
    driver.visit('https://deckshop.pro')
    yield driver
    driver.quit()
