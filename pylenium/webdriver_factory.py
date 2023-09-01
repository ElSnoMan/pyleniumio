""" Factory to build WebDrivers, leveraging Selenium Manager.

The Pylenium class asks for a PyleniumConfig object to build a WebDriver,
so the `build_from_config` method is the "main" method in this module.
"""
from typing import Dict, List, Optional

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.safari.service import Service as SafariService
from selenium.webdriver.remote.webdriver import WebDriver
from seleniumwire import webdriver as wire_driver

from pylenium.config import PyleniumConfig


class Browser:
    """ENUM of supported browsers."""

    CHROME = "chrome"
    EDGE = "edge"
    SAFARI = "safari"
    FIREFOX = "firefox"
    IE = "ie"


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
    elif browser == Browser.EDGE:
        caps.update(webdriver.DesiredCapabilities.EDGE.copy())
    elif browser == Browser.SAFARI:
        caps.update(webdriver.DesiredCapabilities.SAFARI.copy())
    elif browser == Browser.FIREFOX:
        caps.update(webdriver.DesiredCapabilities.FIREFOX.copy())
    elif browser == Browser.IE:
        caps.update(webdriver.DesiredCapabilities.INTERNETEXPLORER.copy())
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
    elif browser == Browser.EDGE:
        options = EdgeOptions()
    elif browser == Browser.SAFARI:
        options = webdriver.SafariOptions()
    elif browser == Browser.FIREFOX:
        options = webdriver.FirefoxOptions()
    elif browser == Browser.IE:
        options = webdriver.IeOptions()
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
    seleniumwire_enabled = config.driver.seleniumwire_enabled
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

    # Set fields for the rest of the non-remote drivers
    _config["local_path"] = config.driver.local_path

    # Build SeleniumWire driver if enabled
    if seleniumwire_enabled:
        if browser == Browser.CHROME:
            return build_chrome(seleniumwire_options=config.driver.seleniumwire_options, **_config)
        if browser == Browser.FIREFOX:
            return build_firefox(seleniumwire_options=config.driver.seleniumwire_options, **_config)
        raise ValueError(f"Only chrome and firefox are supported by SeleniumWire, not {config.driver.browser}")

    # Otherwise, build the driver normally
    if browser == Browser.CHROME:
        return build_chrome(seleniumwire_options=None, **_config)
    if browser == Browser.EDGE:
        return build_edge(**_config)
    if browser == Browser.SAFARI:
        return build_safari(**_config)
    if browser == Browser.FIREFOX:
        return build_firefox(seleniumwire_options=None, **_config)
    if browser == Browser.IE:
        return build_ie(**_config)
    raise ValueError(f"{config.driver.browser} is not supported. Cannot build WebDriver from config.")


def build_chrome(
    options: Optional[List[str]],
    capabilities: Optional[Dict],
    experimental_options: Optional[List[Dict]],
    seleniumwire_options: Optional[Dict],
    extension_paths: Optional[List[str]],
    local_path: Optional[str],
    webdriver_kwargs: Optional[Dict],
):
    """Build a Chrome WebDriver.

    If seleniumwire_options is not None, a SeleniumWire Chrome WebDriver is built.

    Args:
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
    browser_options = build_options(Browser.CHROME, options, experimental_options, extension_paths)
    caps = build_capabilities(Browser.CHROME, capabilities)
    for cap in caps:
        browser_options.set_capability(cap, caps[cap])

    if seleniumwire_options is None:  # default to regular ChromeDriver
        driver = webdriver.Chrome(
            options=browser_options,
            service=ChromeService(local_path or None),
            **(webdriver_kwargs or {}),
        )

    else:
        wire_options = seleniumwire_options or {}
        driver = wire_driver.Chrome(
            service=ChromeService(local_path or None),
            options=browser_options,
            seleniumwire_options=wire_options,
            **(webdriver_kwargs or {}),
        )

    # enable Performance Metrics from Chrome Dev Tools
    driver.execute_cdp_cmd("Performance.enable", {})
    return driver


def build_edge(
    options: Optional[List[str]],
    capabilities: Optional[Dict],
    experimental_options: Optional[List[Dict]],
    extension_paths: Optional[List[str]],
    local_path: Optional[str],
    webdriver_kwargs: Optional[Dict],
) -> WebDriver:
    """Build an Edge WebDriver.

    Args:
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
    for cap in caps:
        browser_options.set_capability(cap, caps[cap])

    return webdriver.Edge(
        service=EdgeService(local_path or None),
        options=browser_options,
        **(webdriver_kwargs or {}),
    )


def build_safari(
    options: Optional[List[str]],
    capabilities: Optional[Dict],
    experimental_options: Optional[List[Dict]],
    extension_paths: Optional[List[str]],
    local_path: Optional[str],
    webdriver_kwargs: Optional[Dict],
) -> WebDriver:
    """Build a Safari WebDriver.

    Args:
        options: The list of options/arguments to include.
        capabilities: The dict of capabilities to include.
        experimental_options: The list of experimental options to include.
        extension_paths: The list of extensions to add to the browser.
        local_path: The path to the driver binary.
        webdriver_kwargs: additional keyword arguments to pass.

    Usage:
        driver = webdriver_factory.build_safari("latest", ["headless"])
    """
    browser_options = build_options(Browser.SAFARI, options, experimental_options, extension_paths)
    caps = build_capabilities(Browser.SAFARI, capabilities)
    for cap in caps:
        browser_options.set_capability(cap, caps[cap])

    return webdriver.Safari(
        options=options,
        service=SafariService(local_path or None),
        **(webdriver_kwargs or {}),
    )


def build_firefox(
    options: Optional[List[str]],
    capabilities: Optional[Dict],
    experimental_options: Optional[List[Dict]],
    seleniumwire_options: Optional[Dict],
    extension_paths: Optional[List[str]],
    local_path: Optional[str],
    webdriver_kwargs: Optional[Dict],
):
    """Build a Firefox WebDriver.

    If seleniumwire_options is not None, a SeleniumWire Firefox WebDriver is built.

    Args:
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
    caps = build_capabilities(Browser.FIREFOX, capabilities)
    browser_options = build_options(Browser.FIREFOX, options, experimental_options, extension_paths)
    for cap in caps:
        browser_options.set_capability(cap, caps[cap])

    if seleniumwire_options is None:  # default to regular FirefoxDriver
        return webdriver.Firefox(
            options=browser_options,
            service=FirefoxService(local_path or None),
            **(webdriver_kwargs or {}),
        )
    else:
        wire_options = seleniumwire_options or {}
        return wire_driver.Firefox(
            options=browser_options,
            service=FirefoxService(local_path or None),
            seleniumwire_options=wire_options,
            **(webdriver_kwargs or {}),
        )


def build_ie(
    options: Optional[List[str]],
    capabilities: Optional[Dict],
    experimental_options: Optional[List[Dict]],
    extension_paths: Optional[List[str]],
    local_path: Optional[str],
    webdriver_kwargs: Optional[Dict],
) -> WebDriver:
    """Build an Internet Explorer WebDriver.

    Args:
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
        executable_path=local_path or None,
        options=browser_options,
        capabilities=caps,
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
