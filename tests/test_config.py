import pytest


def test_py_config_defaults(py_config):
    # driver settings
    assert py_config.driver.browser == 'chrome'
    assert py_config.driver.remote_url == ''
    assert py_config.driver.wait_time == 10
    assert py_config.driver.page_load_wait_time == 0
    assert py_config.driver.options == []
    assert py_config.driver.version == 'latest'
    assert py_config.driver.capabilities == {}
    assert py_config.driver.experimental_options is None

    # logging settings
    assert py_config.logging.screenshots_on is True
    assert py_config.logging.pylog_level == 'info'

    # viewport settings
    assert py_config.viewport.maximize is True
    assert py_config.viewport.width == 1440
    assert py_config.viewport.height == 900
    assert py_config.viewport.orientation == 'portrait'

    # custom settings
    assert py_config.custom is not None


def test_py_config(py_config):
    # driver settings
    assert py_config.driver.browser == 'chrome'
    assert py_config.driver.remote_url == ''
    assert py_config.driver.wait_time == 10
    assert py_config.driver.page_load_wait_time == 0
    assert py_config.driver.options == []
    assert py_config.driver.version == 'latest'
    assert py_config.driver.capabilities == {'name': 'value'}
    assert py_config.driver.experimental_options == [{'name': 'value'}]

    # logging settings
    assert py_config.logging.screenshots_on is True
    assert py_config.logging.pylog_level == 'info'

    # viewport settings
    assert py_config.viewport.maximize is True
    assert py_config.viewport.width == 1440
    assert py_config.viewport.height == 900
    assert py_config.viewport.orientation == 'portrait'

    # custom settings
    assert py_config.custom is not None


@pytest.mark.skip(reason="local test only")
def test_py_config_cli_log_level_off(py_config):
    # cli_log_level = 'off'
    assert py_config.logging.pylog_level == 'off'


@pytest.mark.skip(reason="local test only")
def test_py_config_cli_log_level_info(py_config):
    # cli_log_level = 'info'
    assert py_config.logging.pylog_level == 'info'


@pytest.mark.skip(reason="local test only")
def test_py_config_cli_log_level_debug(py_config):
    # cli_log_level = 'debug'
    assert py_config.logging.pylog_level == 'debug'
