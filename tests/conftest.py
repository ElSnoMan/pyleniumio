import pytest
from pylenium.pydriver import SeleniumDriver


@pytest.fixture
def py():
    driver = SeleniumDriver()
    yield driver
    driver.quit()


@pytest.fixture(scope='module')
def driver():
    driver = SeleniumDriver()
    driver.visit('https://deckshop.pro')
    yield driver
    driver.quit()
