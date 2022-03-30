""" Factory to build WebDrivers.

The Pylenium class asks for a PyleniumConfig object to build a WebDriver,
so the `build_from_config` method is the "main" method in this module.
"""
from typing import Dict, List, Optional

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.remote.webdriver import WebDriver
from seleniumwire import webdriver as wire_driver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager, IEDriverManager
from webdriver_manager.opera import OperaDriverManager

from pylenium.config import PyleniumConfig


class Browser:
    """ENUM of supported browsers."""

    CHROME = "chrome"
    EDGE = "edge"
    FIREFOX = "firefox"
    IE = "ie"
    OPERA = "opera"


def build_capabilities(browser: str, capabilities: Optional[Dict]) -> Dict:
    """Build the capabilities dictionary for the given browser.

    Some WebDrivers pass in capabilities directly, but others (ie Chrome) require it be added via the Options object.

    Args:
        browser: The name of the browser.
        capabilities: The dict of capabilities to include. If None, default caps are used.

    Usage:
        caps = build_capabilities("chrome", {"enableVNC": True, "enableVideo": False})
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
        raise ValueError(f"{browser} is not supported. Cannot build capabilities.")

    if capabilities:
        caps.update(capabilities)

    return caps


def build_options(
    browser: str,
    browser_options: Optional[List[str]],
    experimental_options: Optional[List[Dict]],
    extension_paths: Optional[List[str]],
):
    """Build the Options object for the given browser.

    Args:
        browser: The name of the browser.
        browser_options: The list of options/arguments to include.
        experimental_options: The list of experimental options to include.
        extension_paths: The list of extension filepaths to add to the browser session.

    Usage:
        options = build_options("chrome", ["headless", "incognito"], [{"useAutomationExtension", False}])
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
        options = EdgeOptions()
    else:
        raise ValueError(f"{browser} is not supported. Cannot build options.")

    for option in browser_options:
        if option.startswith("--"):
            options.add_argument(option)
        else:
            options.add_argument(f"--{option}")

    if experimental_options:
        for exp_option in experimental_options:
            ((name, value),) = exp_option.items()
            options.add_experimental_option(name, value)

    if extension_paths:
        for path in extension_paths:
            options.add_extension(path)

    return options


def build_from_config(config: PyleniumConfig) -> WebDriver:
    """The "main" method for building a WebDriver using PyleniumConfig.

    Args:
        config: PyleniumConfig is built using pylenium.json and CLI args.

    Usage:
        driver = webdriver_factory.build_from_config(config)

    Returns:
        An instance of WebDriver.
    """
    browser = config.driver.browser.lower()
    remote_url = config.driver.remote_url
    _config = {
        "options": config.driver.options,
        "capabilities": config.driver.capabilities,
        "experimental_options": config.driver.experimental_options,
        "extension_paths": config.driver.extension_paths,
        "webdriver_kwargs": config.driver.webdriver_kwargs,
    }

    if remote_url:
        # version is passed in as {"browserVersion": version} in capabilities
        return build_remote(browser, remote_url, **_config)

    # Start with SeleniumWire drivers
    # Set fields for the rest of the non-remote drivers
    _config["version"] = config.driver.version
    _config["local_path"] = config.driver.local_path

    if browser == Browser.CHROME:
        return build_chrome(seleniumwire_options=config.driver.seleniumwire_options, **_config)
    if browser == Browser.FIREFOX:
        return build_firefox(seleniumwire_options=config.driver.seleniumwire_options, **_config)

    # Then non-SeleniumWire drivers
    del _config["seleniumwire_options"]

    if browser == Browser.IE:
        return build_ie(**_config)
    elif browser == Browser.OPERA:
        return build_opera(**_config)
    elif browser == Browser.EDGE:
        return build_edge(**_config)
    else:
        raise ValueError(f"{config.driver.browser} is not supported. Cannot build WebDriver from config.")


def build_chrome(
    version: Optional[str],
    options: Optional[List[str]],
    capabilities: Optional[Dict],
    experimental_options: Optional[List[Dict]],
    seleniumwire_options: Optional[Dict],
    extension_paths: Optional[List[str]],
    local_path: Optional[str],
    webdriver_kwargs: Optional[Dict],
):
    """Build a Chrome WebDriver.

    Args:
        version: The desired version of Chrome.
        options: The list of options/arguments to include.
        capabilities: The dict of capabilities to include.
        experimental_options: The list of experimental options to include.
        seleniumwire_options: The dict of seleniumwire options to include.
        extension_paths: The list of extension filepaths to add to the browser.
        local_path: The path to the driver binary (only to bypass WebDriverManager)
        webdriver_kwargs: additional keyword arguments to pass.

    Usage:
        driver = webdriver_factory.build_chrome("latest", ["headless", "incognito"])
    """
    wire_options = seleniumwire_options or {}
    browser_options = build_options(Browser.CHROME, options, experimental_options, extension_paths)
    caps = build_capabilities(Browser.CHROME, capabilities)
    for cap in caps:
        browser_options.set_capability(cap, caps[cap])

    driver = wire_driver.Chrome(
        service=ChromeService(local_path or ChromeDriverManager(version=version).install()),
        options=browser_options,
        seleniumwire_options=wire_options,
        **(webdriver_kwargs or {}),
    )

    # enable Performance Metrics from Chrome Dev Tools
    driver.execute_cdp_cmd("Performance.enable", {})
    return driver


def build_edge(
    version: Optional[str],
    options: Optional[List[str]],
    capabilities: Optional[Dict],
    experimental_options: Optional[List[Dict]],
    extension_paths: Optional[List[str]],
    local_path: Optional[str],
    webdriver_kwargs: Optional[Dict],
) -> WebDriver:
    """Build an Edge WebDriver.

    Args:
        version: The desired version of Edge.
        options: The list of options/arguments to include.
        capabilities: The dict of capabilities to include.
        experimental_options: The list of experimental options to include.
        extension_paths: The list of extensions to add to the browser.
        local_path: The path to the driver binary.
        webdriver_kwargs: additional keyword arguments to pass.

    Usage:
        driver = webdriver_factory.build_edge("latest", ["headless", "incognito"])
    """
    caps = build_capabilities(Browser.EDGE, capabilities)
    browser_options = build_options(Browser.EDGE, options, experimental_options, extension_paths)
    return webdriver.Edge(
        service=EdgeService(local_path or EdgeChromiumDriverManager(version=version).install()),
        capabilities=caps,
        options=browser_options,
        **(webdriver_kwargs or {}),
    )


def build_firefox(
    version: Optional[str],
    options: Optional[List[str]],
    capabilities: Optional[Dict],
    experimental_options: Optional[List[Dict]],
    seleniumwire_options: Optional[Dict],
    extension_paths: Optional[List[str]],
    local_path: Optional[str],
    webdriver_kwargs: Optional[Dict],
):
    """Build a Firefox WebDriver.

    Args:
        version: The desired version of Firefox.
        options: The list of options/arguments to include.
        capabilities: The dict of capabilities to include.
        experimental_options: The list of experimental options to include.
        seleniumwire_options: The dict of seleniumwire options to include.
        extension_paths: The list of extensions to add to the browser.
        local_path: The path to the driver binary.
        webdriver_kwargs: additional keyword arguments to pass.

    Usage:
        driver = webdriver_factory.build_firefox("latest", ["headless", "incognito"])
    """
    wire_options = seleniumwire_options or {}
    caps = build_capabilities(Browser.FIREFOX, capabilities)
    browser_options = build_options(Browser.FIREFOX, options, experimental_options, extension_paths)
    return wire_driver.Firefox(
        service=FirefoxService(local_path or GeckoDriverManager(version=version).install()),
        capabilities=caps,
        options=browser_options,
        seleniumwire_options=wire_options,
        **(webdriver_kwargs or {}),
    )


def build_ie(
    version: Optional[str],
    options: Optional[List[str]],
    capabilities: Optional[Dict],
    experimental_options: Optional[List[Dict]],
    extension_paths: Optional[List[str]],
    local_path: Optional[str],
    webdriver_kwargs: Optional[Dict],
) -> WebDriver:
    """Build an Internet Explorer WebDriver.

    Args:
        version: The desired version of IE.
        options: The list of options/arguments to include.
        capabilities: The dict of capabilities.
        experimental_options: The list of experimental options to include.
        extension_paths: The list of extensions to add to the browser.
        local_path: The path to the driver binary.
        webdriver_kwargs: additional keyword arguments to pass.

    Usage:
        driver = webdriver_factory.build_ie("latest", ["headless"])
    """
    caps = build_capabilities(Browser.IE, capabilities)
    browser_options = build_options(Browser.IE, options, experimental_options, extension_paths)
    return webdriver.Ie(
        executable_path=local_path or IEDriverManager(version=version).install(),
        options=browser_options,
        capabilities=caps,
        **(webdriver_kwargs or {}),
    )


def build_opera(
    version: Optional[str],
    options: Optional[List[str]],
    capabilities: Optional[Dict],
    experimental_options: Optional[List[Dict]],
    extension_paths: Optional[List[str]],
    local_path: Optional[str],
    webdriver_kwargs: Optional[Dict],
) -> WebDriver:
    """Build an Opera WebDriver.

    Args:
        version: The desired version of Opera.
        options: The list of options/arguments to include.
        capabilities: The dict of capabilities to include.
        experimental_options: The list of experimental options to include.
        extension_paths: The list of extensions to add to the browser.
        local_path: The path to the driver binary.
        webdriver_kwargs: additional keyword arguments to pass.

    Usage:
        driver = webdriver_factory.build_opera("latest", ["headless"])
    """
    browser_options = build_options(Browser.OPERA, options, experimental_options, extension_paths)
    caps = build_capabilities(Browser.OPERA, capabilities)
    for cap in caps:
        browser_options.set_capability(cap, caps[cap])

    return webdriver.Opera(
        local_path or OperaDriverManager(version=version).install(),
        options=options,
        **(webdriver_kwargs or {}),
    )


def build_remote(
    browser: str,
    remote_url: str,
    options: Optional[List[str]],
    capabilities: Optional[Dict],
    experimental_options: Optional[List[Dict]],
    extension_paths: Optional[List[str]],
    webdriver_kwargs: Optional[Dict],
):
    """Build a RemoteDriver connected to a Grid.

    Args:
        browser: Name of the browser to connect to.
        remote_url: The URL to connect to the Grid.
        browser_options: The list of options/arguments to include.
        capabilities: The dict of capabilities to include.
        experimental_options: The list of experimental options to include.
        extension_paths: The list of extensions to add to the browser.
        webdriver_kwargs: additional keyword arguments to pass.

    Usage:
        driver = webdriver_factory.build_remote("chrome", "http://localhost:4444/wd/hub", ["headless"])

    Returns:
        The instance of WebDriver once the connection is successful
    """
    caps = build_capabilities(browser, capabilities)
    browser_options = build_options(browser, options, experimental_options, extension_paths)
    for cap in caps:
        browser_options.set_capability(cap, caps[cap])

    return webdriver.Remote(
        command_executor=remote_url,
        options=browser_options,
        **(webdriver_kwargs or {}),
    )
