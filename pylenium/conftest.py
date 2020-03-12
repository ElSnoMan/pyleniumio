"""
`conftest.py` and `pylenium.json` files should stay at your Workspace Root.

conftest.py
    Although this file is editable, you should only change its contents if you know what you are doing.

pylenium.json
    You can change the values, but DO NOT touch the keys.
"""

import os
import json
import pytest
from pylenium import Pylenium
from pylenium.config import PyleniumConfig


@pytest.fixture(scope='session')
def workspace_root():
    """ Your project's root directory (aka Workspace Root) """
    return os.path.dirname(os.path.abspath(__file__))


@pytest.fixture
def py_config(workspace_root):
    """ Initialize a PyleniumConfig for each test using pylenium.json """
    with open(f'{workspace_root}/pylenium.json') as file:
        _json = json.load(file)
    return PyleniumConfig(**_json)


@pytest.fixture
def py(py_config):
    """ Initialize a Pylenium driver for each test.

    Pass in this `py` fixture into the test function.

    Examples:
        def test_go_to_google(py):
            py.visit('https://google.com')
            assert 'Google' in py.title
    """
    py = Pylenium(py_config)
    yield py
    py.quit()
