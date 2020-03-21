""" Factory to build WebDrivers. """
from typing import List

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from pylenium.config import PyleniumConfig


def build_options(browser, browser_options: List[str]):
    """ Build the Options object for Chrome or Firefox.

    Args:
        browser: The name of the browser.
        browser_options: The list of options/arguments to include.

    Raises:
        ValueError if browser is not 'chrome' or 'firefox'

    Examples:
        driver = WebDriverFactory().build_chrome(['headless', 'incognito'])
    """
    if browser == 'chrome':
        options = webdriver.ChromeOptions()
    elif browser == 'firefox':
        options = webdriver.FirefoxOptions()
    else:
        options = None

    if options:
        for option in browser_options:
            options.add_argument(f'--{option}')
        return options
    else:
        raise ValueError(f'{browser} is not currently supported. Try "chrome" or "firefox" instead.')


def build_from_config(config: PyleniumConfig) -> WebDriver:
    """ Build a WebDriver using PyleniumConfig.

    PyleniumConfig is built using pylenium.json and CLI args.
    """
    if config.driver.remote_url:
        return build_remote(
            browser=config.driver.browser,
            remote_url=config.driver.remote_url,
            browser_options=config.driver.options
        )
    if config.driver.browser == 'chrome':
        return build_chrome(config.driver.options)
    elif config.driver.browser == 'firefox':
        return build_firefox(config.driver.options)


def build_chrome(browser_options: List[str]) -> WebDriver:
    """ Build a ChromeDriver.

    Args:
        browser_options: The list of options/arguments to include.

    Examples:
        driver = WebDriverFactory().build_chrome(['headless', 'incognito'])
    """
    options = build_options('chrome', browser_options)
    return webdriver.Chrome(options=options)


def build_firefox(browser_options: List[str]) -> WebDriver:
    """ Build a FirefoxDriver.

    Args:
        browser_options: The list of options/arguments to include.

    Examples:
        driver = WebDriverFactory().build_firefox(['headless', 'incognito'])
    """
    options = build_options('firefox', browser_options)
    return webdriver.Firefox(options=options)


def build_remote(browser: str, remote_url: str, browser_options: List[str]) -> WebDriver:
    """ Build a RemoteDriver connected to a Grid.

    Args:
        browser: Name of the browser to connect to.
        remote_url: The URL to connect to the Grid.
        browser_options: The list of options/arguments to include.

    Returns:
        The instance of WebDriver once the connection is successful
    """
    if browser == 'chrome':
        caps = webdriver.DesiredCapabilities.CHROME.copy()
    elif browser == 'firefox':
        caps = webdriver.DesiredCapabilities.FIREFOX.copy()
    else:
        caps = None

    options = build_options(browser, browser_options)

    return webdriver.Remote(
        command_executor=remote_url,
        desired_capabilities=caps,
        options=options
    )
