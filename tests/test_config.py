import pytest


def test_py_config_defaults(py_config):
    # driver settings
    assert py_config.driver.browser == 'chrome'
    assert py_config.driver.remote_url == ''
    assert py_config.driver.wait_time == 10
    assert py_config.driver.options == []

    # logging settings
    assert py_config.logging.screenshots_on is True
    assert py_config.logging.pylog_level == 'info'

    # viewport settings
    assert py_config.viewport.maximize is True
    assert py_config.viewport.width == 1440
    assert py_config.viewport.height == 900
    assert py_config.viewport.orientation == 'portrait'


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
