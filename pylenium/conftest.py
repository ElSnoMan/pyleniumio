import json
import pytest
from pylenium import Pylenium
from pylenium.config import PyleniumConfig


@pytest.fixture
def py_config():
    with open('../pylenium/config/pylenium.json') as file:
        _json = json.load(file)
    return PyleniumConfig(**_json)


@pytest.fixture
def py(py_config):
    py = Pylenium(py_config)
    yield py
    py.quit()
