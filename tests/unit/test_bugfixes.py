from unittest.mock import patch, MagicMock
from pylenium import webdriver_factory


def test_235_webdriver_factory(tmpdir):
    file_to_use = tmpdir / "file"
    file_to_use.write("test")
    gecko_mock = MagicMock()
    gecko_mock.install.return_value = file_to_use
    with patch("pylenium.webdriver_factory.GeckoDriverManager", return_value=gecko_mock):
        with patch("pylenium.webdriver_factory.webdriver.firefox.webdriver.Service"):
            with patch("pylenium.webdriver_factory.webdriver.firefox.webdriver.RemoteWebDriver"):
                webdriver_factory.build_firefox("latest", ["headless"], {}, [], [], "", {})
                gecko_mock.install.assert_called_once()
