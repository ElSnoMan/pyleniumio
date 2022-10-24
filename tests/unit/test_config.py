def test_py_config_defaults(py_config):
    # driver settings
    assert py_config.driver.browser == "chrome"
    assert py_config.driver.remote_url == ""
    assert py_config.driver.wait_time == 10
    assert py_config.driver.page_load_wait_time == 0
    assert py_config.driver.options == []
    assert py_config.driver.version == ""
    assert py_config.driver.capabilities == {}
    assert py_config.driver.experimental_options is None
    assert py_config.driver.webdriver_kwargs == {}
    assert py_config.driver.seleniumwire_options == {}

    # logging settings
    assert py_config.logging.screenshots_on is True
    assert py_config.logging.pylog_level == "INFO"

    # viewport settings
    assert py_config.viewport.maximize is True
    assert py_config.viewport.width == 1440
    assert py_config.viewport.height == 900
    assert py_config.viewport.orientation == "portrait"

    # custom settings
    assert py_config.custom is not None
