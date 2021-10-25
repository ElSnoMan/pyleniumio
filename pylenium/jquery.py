from selenium.webdriver.remote.webdriver import WebDriver, By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
from pylenium import utils


def inject(driver: WebDriver, version="3.5.1", timeout=10):
    """Inject the given jQuery version to the current context and any iframes within it.

    Args:
        driver: The instance of WebDriver to attach to.
        version: The jQuery version. (Default is 3.5.1)
        timeout: The max number of seconds to wait for jQuery to be loaded. (Default is 10)
    """
    jquery_url = f"https://code.jquery.com/jquery-{version}.min.js"
    load_jquery = utils.read_script_from_file("load_jquery.js")
    driver.execute_async_script(load_jquery, jquery_url, None)
    WebDriverWait(driver, timeout).until(
        lambda drvr: drvr.execute_script('return typeof(jQuery) !== "undefined";'),
        message='jQuery was "undefined" which means it did not load within timeout.',
    )
    iframes = driver.find_elements(By.TAG_NAME, "iframe")
    for iframe in iframes:
        try:
            driver.execute_async_script(load_jquery, jquery_url, iframe)
        except StaleElementReferenceException:
            pass


def exists(driver: WebDriver) -> str:
    """Checks if jQuery exists in the current context.

    Returns:
        The version if found, else returns an empty string
    """
    version = driver.execute_script("return jQuery().jquery;")
    return version if version is not None else ""


def drag_and_drop(driver: WebDriver, drag_element: WebElement, drop_element: WebElement, version="3.5.1", timeout=10):
    """Simulate Drag and Drop using jQuery.

    Args:
        driver: The driver that will simulate the drag and drop.
        drag_element: The element to be dragged.
        drop_element: The element to drop to.
        version: The jQuery version to use.
        timeout: The max of number of seconds to wait for jQuery to be loaded.
    """
    inject(driver, version)
    dnd_js = utils.read_script_from_file("drag_and_drop.js")
    driver.execute_script(
        dnd_js + "jQuery(arguments[0]).simulateDragDrop({ dropTarget: arguments[1] });", drag_element, drop_element
    )
