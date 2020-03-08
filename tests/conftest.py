import pytest
from pylenium.pydriver import SeleniumDriver


@pytest.fixture
def driver():
    driver = SeleniumDriver()
    yield driver
    driver.quit()
