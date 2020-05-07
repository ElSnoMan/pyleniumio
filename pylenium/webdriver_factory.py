""" Factory to build WebDrivers. """
from typing import List, Optional

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager, EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager
from selenium.webdriver.edge.options import Options
from pylenium.config import PyleniumConfig


class Browser:
    """ ENUM of supported browsers. """
    CHROME = 'chrome'
    EDGE = 'edge'
    FIREFOX = 'firefox'
    IE = 'ie'
    OPERA = 'opera'


def build_capabilities(browser, capabilities: dict):
    """ Build the capabilities dictionary for WebDriver.

    Args:
        browser: The name of the browser.
        capabilities: The dict of capabilities to include.

    Examples:
        caps = WebDriverFactory().build_capabilities({'enableVNC': True, 'enableVideo': False})
    """
    caps = {}

    if browser == Browser.CHROME:
        caps.update(webdriver.DesiredCapabilities.CHROME.copy())
    elif browser == Browser.FIREFOX:
        caps.update(webdriver.DesiredCapabilities.FIREFOX.copy())
    elif browser == Browser.IE:
        caps.update(webdriver.DesiredCapabilities.INTERNETEXPLORER.copy())
    elif browser == Browser.OPERA:
        caps.update(webdriver.DesiredCapabilities.OPERA.copy())
    elif browser == Browser.EDGE:
        caps.update(webdriver.DesiredCapabilities.EDGE.copy())
    else:
        raise ValueError(f'{browser} is not supported.')

    if capabilities:
        caps.update(capabilities)

    return caps


def build_options(browser,
                  browser_options: List[str],
                  experimental_options: Optional[List[dict]],
                  extension_paths: Optional[List[str]]):
    """ Build the Options object for Chrome or Firefox.

    Args:
        browser: The name of the browser.
        browser_options: The list of options/arguments to include.
        experimental_options: The list of experimental options to include.
        extension_paths: The list of extensions to add to the browser session.

    Examples:
        WebDriverFactory().build_options('chrome', ['headless', 'incognito'], [{'useAutomationExtension', False}])
    """
    browser = browser.lower()
    if browser == Browser.CHROME:
        options = webdriver.ChromeOptions()
    elif browser == Browser.FIREFOX:
        options = webdriver.FirefoxOptions()
    elif browser == Browser.IE:
        options = webdriver.IeOptions()
    elif browser == Browser.OPERA:
        options = webdriver.ChromeOptions()
    elif browser == Browser.EDGE:
        options = Options()
    else:
        raise ValueError(f'{browser} is not supported. https://elsnoman.gitbook.io/pylenium/configuration/driver')

    for option in browser_options:
        options.add_argument(f'--{option}')

    if experimental_options:
        for exp_option in experimental_options:
            (name, value), = exp_option.items()
            options.add_experimental_option(name, value)

    if extension_paths:
        for path in extension_paths:
            options.add_extension(path)

    return options


def build_from_config(config: PyleniumConfig) -> WebDriver:
    """ Build a WebDriver using PyleniumConfig.

    PyleniumConfig is built using pylenium.json and CLI args.
    """
    if config.driver.remote_url:
        return build_remote(
            browser=config.driver.browser,
            remote_url=config.driver.remote_url,
            browser_options=config.driver.options,
            capabilities=config.driver.capabilities,
            experimental_options=config.driver.experimental_options,
            extension_paths=config.driver.extension_paths
        )
    browser = config.driver.browser.lower()
    if browser == Browser.CHROME:
        return build_chrome(config.driver.version, config.driver.options, config.driver.experimental_options, config.driver.extension_paths)
    elif browser == Browser.FIREFOX:
        return build_firefox(config.driver.version, config.driver.options, config.driver.experimental_options, config.driver.extension_paths)
    elif browser == Browser.IE:
        return build_ie(config.driver.version, config.driver.options, config.driver.capabilities, config.driver.experimental_options, config.driver.extension_paths)
    elif browser == Browser.OPERA:
        return build_opera(config.driver.version, config.driver.options, config.driver.experimental_options, config.driver.extension_paths)
    elif browser == Browser.EDGE:
        return build_edge(config.driver.version, config.driver.options, config.driver.capabilities, config.driver.experimental_options, config.driver.extension_paths)
    else:
        raise ValueError(f'{config.driver.browser} is not supported. https://elsnoman.gitbook.io/pylenium/configuration/driver')


def build_chrome(version: str,
                 browser_options: List[str],
                 experimental_options: Optional[List[dict]],
                 extension_paths: Optional[List[str]]) -> WebDriver:
    """ Build a ChromeDriver.

    Args:
        version: The desired version of Chrome.
        browser_options: The list of options/arguments to include.
        experimental_options: The list of experimental options to include.
        extension_paths: The list of extensions to add to the browser.

    Examples:
        driver = WebDriverFactory().build_chrome('latest', ['headless', 'incognito'], None)
    """
    options = build_options(Browser.CHROME, browser_options, experimental_options, extension_paths)
    return webdriver.Chrome(ChromeDriverManager(version=version).install(), options=options)


def build_edge(version: str,
               browser_options: List[str],
               capabilities: dict,
               experimental_options: Optional[List[dict]],
               extension_paths: Optional[List[str]]) -> WebDriver:
    """ Build a Edge Driver.

    Args:
        version: The desired version of Edge.
        browser_options: The list of options/arguments to include.
        capabilities: The dict of capabilities to include.
        experimental_options: The list of experimental options to include.
        extension_paths: The list of extensions to add to the browser.

    Examples:
        driver = WebDriverFactory().build_edge('latest', ['headless', 'incognito'], None)
    """
    caps = build_capabilities(Browser.EDGE, capabilities)
    options = build_options(Browser.EDGE, browser_options, experimental_options, extension_paths).to_capabilities()
    caps.update(options)
    return webdriver.Edge(EdgeChromiumDriverManager(version=version).install(),  capabilities=caps)


def build_firefox(version: str,
                  browser_options: List[str],
                  experimental_options: Optional[List[dict]],
                  extension_paths: Optional[List[str]]) -> WebDriver:
    """ Build a FirefoxDriver.

    Args:
        version: The desired version of Firefox.
        browser_options: The list of options/arguments to include.
        experimental_options: The list of experimental options to include.
        extension_paths: The list of extensions to add to the browser.

    Examples:
        driver = WebDriverFactory().build_firefox('latest', ['headless', 'incognito'], None)
    """
    options = build_options(Browser.FIREFOX, browser_options, experimental_options, extension_paths)
    return webdriver.Firefox(executable_path=GeckoDriverManager(version=version).install(), options=options)


def build_ie(version: str,
             browser_options: List[str],
             capabilities: dict,
             experimental_options: Optional[List[dict]],
             extension_paths: Optional[List[str]]) -> WebDriver:
    """ Build an IEDriver.

    Args:
        version: The desired version of IE.
        browser_options: The list of options/arguments to include.
        capabilities: The dict of capabilities.
        experimental_options: The list of experimental options to include.
        extension_paths: The list of extensions to add to the browser.

    Examples:
        driver = WebDriverFactory().build_ie('latest', ['headless'], None)
    """
    caps = build_capabilities(Browser.IE, capabilities)
    options = build_options(Browser.IE, browser_options, experimental_options, extension_paths)
    return webdriver.Ie(executable_path=IEDriverManager(version=version).install(), options=options, capabilities=caps)


def build_opera(version: str,
                browser_options: List[str],
                experimental_options: Optional[List[dict]],
                extension_paths: Optional[List[str]]) -> WebDriver:
    """ Build an OperaDriver.

    Args:
        version: The desired version of Opera.
        browser_options: The list of options/arguments to include.
        experimental_options: The list of experimental options to include.
        extension_paths: The list of extensions to add to the browser.

    Examples:
        driver = WebDriverFactory().build_opera('latest', ['--start-maximized'], None)
    """
    options = build_options(Browser.OPERA, browser_options, experimental_options, extension_paths)
    return webdriver.Opera(executable_path=OperaDriverManager(version=version).install(), options=options)


def build_remote(browser: str,
                 remote_url: str,
                 browser_options: List[str],
                 capabilities: dict,
                 experimental_options: Optional[List[dict]],
                 extension_paths: Optional[List[str]]) -> WebDriver:
    """ Build a RemoteDriver connected to a Grid.

    Args:
        browser: Name of the browser to connect to.
        remote_url: The URL to connect to the Grid.
        browser_options: The list of options/arguments to include.
        capabilities: The dict of capabilities to include.
        experimental_options: The list of experimental options to include.
        extension_paths: The list of extensions to add to the browser.

    Returns:
        The instance of WebDriver once the connection is successful
    """
    browser = browser.lower()
    caps = build_capabilities(browser, capabilities)
    options = build_options(browser, browser_options, experimental_options, extension_paths)

    return webdriver.Remote(
        command_executor=remote_url,
        desired_capabilities=caps,
        options=options
    )
