

def test_pylenium_config_defaults(py_config):
    assert py_config.wait_time == 10
