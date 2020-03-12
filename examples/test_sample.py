""" Use @pytest.fixtures when writing UI or end-to-end tests. """


import pytest
from selenium.webdriver.common.keys import Keys
from pylenium import Pylenium


@pytest.fixture
def py_():
    # Code before `yield` is executed Before Each test.
    # By default, fixtures are mapped to each test.
    # You can change the scope by using:
    # `@pytest.fixture(scope=SCOPE)` where SCOPE is 'class', 'module' or 'session'
    _py = Pylenium()

    # Then `yield` or `return` the instance of Pylenium
    yield _py

    # Code after `yield` is executed After Each test.
    # In this case, once the test is complete, quit the driver.
    # This will be executed whether the test passed or failed.
    _py.quit()


def test_using_fixture(py_):
    """ You pass in the name of the fixture as seen on the line above.

    This is the RECOMMENDED option when writing automated tests.
    To find more info on PyTest and Fixtures, go to their docs:

    https://docs.pytest.org/en/latest/fixture.html

    * You can pass in any number of fixtures and fixtures can call other fixtures!
    * You can store fixtures locally in test files or in conftest.py global files
    """
    py_.visit('https://google.com')
    py_.get('[name="q"]').type('puppies', Keys.ENTER)
    assert 'puppies' in py_.title
