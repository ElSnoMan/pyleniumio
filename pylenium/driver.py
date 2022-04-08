import logging
from typing import List, Union

from faker import Faker
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from pylenium import webdriver_factory
from pylenium.cdp import CDP
from pylenium.config import PyleniumConfig
from pylenium.element import Element, Elements
from pylenium.performance import Performance
from pylenium.switch_to import SwitchTo
from pylenium.wait import PyleniumWait


class PyleniumShould:
    def __init__(self, py: "Pylenium", timeout: int, ignored_exceptions: list = None):
        self._py = py
        self._wait: PyleniumWait = self._py.wait(timeout=timeout, use_py=True, ignored_exceptions=ignored_exceptions)

    def have_title(self, title: str) -> "Pylenium":
        """An expectation that the title matches the given title.

        Args:
            title: The title to match.

        Returns:
            The current instance of Pylenium.

        Raises:
            `AssertionError` if the condition is not met within the timeout.
        """
        self._py.log.debug("[ASSERT] .should().have_title()")
        try:
            value = self._wait.until(ec.title_is(title))
        except TimeoutException:
            value = False
        if value:
            return self._py
        else:
            self._py.log.critical(".should().have_title()")
            raise AssertionError(f"Expected Title: ``{title}`` - Actual Title: ``{self._py.title()}``")

    def contain_title(self, string: str) -> "Pylenium":
        """An expectation that the title contains the given string.

        Args:
            string: The case-sensitive string for the title to contain.

        Returns:
            The current instance of Pylenium.

        Raises:
            `AssertionError` if the condition is not met within the timeout.
        """
        self._py.log.debug("[ASSERT] .should().contain_title()")
        try:
            value = self._wait.until(ec.title_contains(string))
        except TimeoutException:
            value = False
        if value:
            return self._py
        else:
            self._py.log.critical(".should().contain_title()")
            raise AssertionError(f"Expected ``{string}`` to be in ``{self._py.title()}``")

    def have_url(self, url: str) -> "Pylenium":
        """An expectation that the URL matches the given url.

        Args:
            url: The url to match.

        Returns:
            The current instance of Pylenium.

        Raises:
            `AssertionError` if the condition is not met within the timeout.
        """
        self._py.log.debug("[ASSERT] .should().have_url()")
        try:
            value = self._wait.until(ec.url_to_be(url))
        except TimeoutException:
            value = False
        if value:
            return self._py
        else:
            self._py.log.critical(".should().have_url()")
            raise AssertionError(f"Expected URL: ``{url}`` - Actual URL: ``{self._py.url()}``")

    def contain_url(self, string: str) -> "Pylenium":
        """An expectation that the URL contains the given string.

        Args:
            string: The case-sensitive string for the url to contain.

        Returns:
            The current instance of Pylenium.

        Raises:
            `AssertionError` if the condition is not met within the timeout.
        """
        self._py.log.debug("[ASSERT] .should().contain_url()")
        try:
            value = self._wait.until(ec.url_contains(string))
        except TimeoutException:
            value = False
        if value:
            return self._py
        else:
            self._py.log.critical(".should().contain_url()")
            raise AssertionError(f"Expected ``{string}`` to be in ``{self._py.url()}``")

    def not_find(self, css: str) -> bool:
        """An expectation that there are no elements with the given CSS in the DOM.

        Args:
            css: The CSS selector.

        Returns:
            True if no elements are found.

        Raises:
            `AssertionError` if the condition is not met within the timeout.
        """
        self._py.log.debug("[ASSERT] .should().not_find()")
        try:
            self._wait.until_not(lambda x: x.find_element(By.CSS_SELECTOR, css))
            return True
        except TimeoutException:
            self._py.log.critical(".should().not_find()")
            raise AssertionError(f"Found element with css: ``{css}``")

    def not_findx(self, xpath: str) -> bool:
        """An expectation that there are no elements with the given XPATH in the DOM.

        Args:
            xpath: The XPATH selector.

        Returns:
            True if no elements are found.

        Raises:
            `AssertionError` if the condition is not met within the timeout.
        """
        self._py.log.debug("[ASSERT] .should().not_find_xpath()")
        try:
            self._wait.until_not(lambda x: x.find_element(By.XPATH, xpath))
            return True
        except TimeoutException:
            self._py.log.critical(".should().not_findx()")
            raise AssertionError(f"Found element with xpath: ``{xpath}``")

    def not_contain(self, text: str) -> bool:
        """An expectation that there are no elements with the given text in the DOM.

        Args:
            text: The text to contain.

        Returns:
            True if no elements are found.

        Raises:
            `AssertionError` if the condition is not met within the timeout.
        """
        self._py.log.debug("[ASSERT] .should().not_contain()")
        try:
            self._wait.until_not(lambda x: x.find_element(By.XPATH, f'//*[contains(text(), "{text}")]'))
            return True
        except TimeoutException:
            self._py.log.critical(".should().not_contain()")
            raise AssertionError(f"Found element containing text: ``{text}``")


class Pylenium:
    """The Pylenium API.

    V1.5.1+: Chrome is the default local browser

    Other supported browsers:
        * Firefox
        * Edge Chromium
        * IE
        * Opera
    """

    def __init__(self, config: PyleniumConfig):
        self.config = config
        self.log = logging.getLogger(__name__)
        self.fake = Faker()
        self.Keys = Keys
        self._webdriver = None
        self._wait = None

    def init_webdriver(self):
        """Initialize WebDriver using the Pylenium Config."""
        self._webdriver = webdriver_factory.build_from_config(self.config)
        caps = self._webdriver.capabilities
        try:
            self.log.debug(
                f"Capabilities: "
                f'browserName: {caps["browserName"]}, browserVersion: {caps["browserVersion"]}, '
                f'platformName: {caps["platformName"]}, session_id: {self._webdriver.session_id}'
            )
        except:
            self.log.warning(
                "webdriver.capabilities did not have a key that Pylenium was expecting. "
                "Is your driver executable the right version?"
            )

        # Default instance of PyleniumWait
        self._wait = PyleniumWait(self, self._webdriver, self.config.driver.wait_time, ignored_exceptions=None)

        # Initial Browser Setup
        if self.config.driver.page_load_wait_time:
            self.set_page_load_timeout(self.config.driver.page_load_wait_time)

        if self.config.viewport.maximize:
            self.maximize_window()
        else:
            self.viewport(self.config.viewport.width, self.config.viewport.height, self.config.viewport.orientation)
        return self._webdriver

    @property
    def webdriver(self) -> WebDriver:
        """The current instance of Selenium's `WebDriver` API."""
        return self.init_webdriver() if self._webdriver is None else self._webdriver

    @property
    def performance(self) -> Performance:
        """The Pylenium Performance API."""
        return Performance(self.webdriver)

    @property
    def cdp(self) -> CDP:
        """The Chrome DevTools Protocol API."""
        return CDP(self.webdriver)

    def title(self) -> str:
        """The current page's title."""
        self.log.debug("[STEP] py.title() - Get the current page title")
        return self.webdriver.title

    def url(self) -> str:
        """The current page's URL."""
        self.log.debug("[STEP] py.url() - Get the current page URL")
        return self.webdriver.current_url

    # NAVIGATION #
    ##############

    def visit(self, url: str) -> "Pylenium":
        """Navigate to the given URL.

        Returns:
            `py` so you can chain another command if needed.
        """
        self.log.debug(f"[STEP] py.visit() - Visit URL: ``{url}``")
        self.webdriver.get(url)
        return self

    def go(self, direction: str, number: int = 1) -> "Pylenium":
        """Navigate forward or back.

        This command executes `window.history.go(number)`

        Args:
            direction: 'forward' or 'back'
            number: default is 1, will go back or forward one page in history.

        Examples:
            `py.go('back', 2)` will go back 2 pages in history.
            `py.go('forward')` will go forward 1 page in history.

        Returns:
            The current instance of Pylenium so you can chain commands.
        """
        self.log.debug(f"[STEP] py.go() - Go {direction} {number} in browser history")
        if direction == "back":
            self.webdriver.execute_script("window.history.go(arguments[0])", number * -1)
        elif direction == "forward":
            self.webdriver.execute_script("window.history.go(arguments[0])", number)
        else:
            raise ValueError(f"direction was invalid. Must be `forward` or `back` but was {direction}")
        return self

    def reload(self) -> "Pylenium":
        """Reloads the current window."""
        self.log.debug("[STEP] py.reload() - Reload the current page")
        self.webdriver.refresh()
        return self

    # region FIND ELEMENTS

    def contains(self, text: str, timeout: int = None) -> Element:
        """Get the DOM element containing the `text`.

        * If timeout=None (default), use the default wait_time.
        * If timeout > 0, override the default wait_time.
        * If timeout=0, poll the DOM immediately without any waiting.

        Args:
            text: The text for the element to contain.
            timeout: The number of seconds to wait for this to succeed. Overrides the default wait_time.

        Returns:
            The first element that is found, even if multiple elements match the query.
        """
        self.log.debug(f"[STEP] py.contains() - Find the element with text: ``{text}``")
        locator = (By.XPATH, f'//*[contains(text(), "{text}")]')

        if timeout == 0:
            element = self.webdriver.find_element(*locator)
        else:
            element = self.wait(timeout).until(
                lambda x: x.find_element(*locator), f"Could not find element with the text ``{text}``"
            )
        return Element(self, element, locator)

    def get(self, css: str, timeout: int = None) -> Element:
        """Get the DOM element that matches the `css` selector.

        * If timeout=None (default), use the default wait_time.
        * If timeout > 0, override the default wait_time.
        * If timeout=0, poll the DOM immediately without any waiting.

        Args:
            css: The selector to use.
            timeout: The number of seconds to wait for this to succeed. Overrides the default wait_time.

        Returns:
            The first element that is found, even if multiple elements match the query.
        """
        self.log.debug(f"[STEP] py.get() - Find the element with css: ``{css}``")
        by = By.CSS_SELECTOR

        if timeout == 0:
            element = self.webdriver.find_element(by, css)
        else:
            element = self.wait(timeout).until(
                lambda x: x.find_element(by, css), f"Could not find element with the CSS ``{css}``"
            )
        return Element(self, element, locator=(by, css))

    def find(self, css: str, timeout: int = None) -> Elements:
        """Finds all DOM elements that match the `css` selector.

        * If timeout=None (default), use the default wait_time.
        * If timeout > 0, override the default wait_time.
        * If timeout=0, poll the DOM immediately without any waiting.

        Args:
            css: The selector to use.
            timeout: The number of seconds to wait for this to succeed. Overrides the default wait_time.

        Returns:
            A list of the found elements.
        """
        by = By.CSS_SELECTOR
        self.log.debug(f"[STEP] py.find() - Find elements with css: ``{css}``")

        try:
            if timeout == 0:
                elements = self.webdriver.find_elements(by, css)
            else:
                elements = self.wait(timeout).until(
                    lambda x: x.find_elements(by, css), f"Could not find any elements with the CSS ``{css}``"
                )
        except TimeoutException:
            elements = []
        return Elements(self, elements, locator=(by, css))

    def getx(self, xpath: str, timeout: int = None) -> Element:
        """Finds the DOM element that match the `xpath` selector.

        * If timeout=None (default), use the default wait_time.
        * If timeout > 0, override the default wait_time.
        * If timeout=0, poll the DOM immediately without any waiting.

        Args:
            xpath: The selector to use.
            timeout: The number of seconds to wait for this to succeed. Overrides the default wait_time.

        Returns:
            The first element that is found, even if multiple elements match the query.
        """
        by = By.XPATH
        self.log.debug(f"[STEP] py.getx() - Find the element with xpath: ``{xpath}``")

        if timeout == 0:
            element = self.webdriver.find_element(by, xpath)
        else:
            element = self.wait(timeout).until(
                lambda x: x.find_element(by, xpath), f"Could not find an element with xpath: ``{xpath}``"
            )
        return Element(self, element, locator=(by, xpath))

    def findx(self, xpath: str, timeout: int = None) -> Elements:
        """Finds the DOM elements that match the `xpath` selector.

        * If timeout=None (default), use the default wait_time.
        * If timeout > 0, override the default wait_time.
        * If timeout=0, poll the DOM immediately without any waiting.

        Args:
            xpath: The selector to use.
            timeout: The number of seconds to wait for this to succeed. Overrides the default wait_time.

        Returns:
            A list of the found elements.
        """
        by = By.XPATH
        self.log.debug(f"[STEP] py.findx() - Find elements with xpath: ``{xpath}``")

        try:
            if timeout == 0:
                elements = self.webdriver.find_elements(by, xpath)
            else:
                elements = self.wait(timeout).until(
                    lambda x: x.find_elements(by, xpath), f"Could not find an element with xpath: ``{xpath}``"
                )
        except TimeoutException:
            elements = []
        return Elements(self, elements, locator=(by, xpath))

    # endregion

    # EXPECTATIONS #
    ################

    def should(self, timeout: int = 0, ignored_exceptions: list = None) -> PyleniumShould:
        """A collection of expectations for this driver.

        Examples:
            py.should().contain_title('QA at the Point')
            py.should().have_url('https://qap.dev')
        """
        if timeout:
            wait_time = timeout
        else:
            wait_time = self.config.driver.wait_time
        return PyleniumShould(self, wait_time, ignored_exceptions)

    # UTILITIES #
    #############

    def screenshot(self, filename: str) -> str:
        """Take a screenshot of the current Window.

        Args:
            filename: the filepath including the filename and extension (like `.png`)

        Examples:
            py.screenshot('screenshots/home_page.png')
        """
        self.log.debug(f"[STEP] py.screenshot() - Save screenshot to: {filename}")
        self.webdriver.save_screenshot(filename)
        return filename

    def scroll_to(self, x, y) -> "Pylenium":
        """Scroll to a location on the page.

        Args:
            x: The number of pixels to scroll horizontally.
            y: The number of pixels to scroll vertically.

        Examples:
            # Scroll down 500 px
            py.scroll_to(0, 500)
        """
        self.log.debug(f"[STEP] py.scroll_to() - Scroll to ({x}, {y})")
        js = "window.scrollTo(arguments[0], arguments[1]);"
        self.webdriver.execute_script(js, x, y)
        return self

    def wait(
        self, timeout: int = None, use_py: bool = False, ignored_exceptions: list = None
    ) -> Union[WebDriverWait, PyleniumWait]:
        """The Wait object with the given timeout in seconds.

        If timeout=None or timeout=0,
        return the default instance of wait, else return a new instance of WebDriverWait or PyleniumWait.

        Args:
            timeout: The number of seconds to wait for the condition.
            use_py: True for a PyleniumWait.
            ignored_exceptions: List of exceptions for the condition to ignore.

        Default Ignored Exceptions:
            * NoSuchElementException

        Examples:
            # use the default wait_time in pylenium.json
            py.wait().until(lambda x: x.find_element(By.ID, 'foo').get_attribute('style') == 'display: block;')
            # use a different timeout to control how long to wait for
            py.wait(5).until(lambda x: x.find_element(By.ID, 'foo').is_displayed())
            py.wait(15, [NoSuchElementException, WebDriverException]).until(lambda x: x.find_element(By.ID, 'foo'))
        """
        if timeout:  # if not None and greater than 0
            return self._wait.build(timeout, use_py, ignored_exceptions)
        else:
            return self._wait.build(self.config.driver.wait_time, use_py, ignored_exceptions)

    # BROWSER #
    ###########

    def delete_cookie(self, name):
        """Deletes the cookie with the given name.

        Examples:
            `py.delete_cookie('cookie_name')`
        """
        self.log.debug(f"py.delete_cookie() - Delete cookie named: {name}")
        self.webdriver.delete_cookie(name)

    def delete_all_cookies(self):
        """Delete all cookies in the current session."""
        self.log.debug("py.delete_all_cookies() - Delete all cookies")
        self.webdriver.delete_all_cookies()

    def get_cookie(self, name) -> dict:
        """Get the cookie with the given name.

        Returns:
            The cookie if found, else None.

        Examples:
            py.get_cookie('cookie_name')
        """
        self.log.debug(f"py.get_cookie() - Get cookie with name: {name}")
        return self.webdriver.get_cookie(name)

    def get_cookies(self):
        """Get all cookies."""
        self.log.debug("py.get_cookies() - Get all cookies")
        return self.webdriver.get_cookies()

    def set_cookie(self, cookie: dict):
        """Adds a cookie to your current session.

        Args:
            cookie: A dictionary object, with required keys: "name" and "value";
                * optional keys: "path", "domain", "secure", "expiry"

        Examples:
            `py.set_cookie({'name' : 'foo', 'value' : 'bar'})`
            `py.set_cookie({'name' : 'foo', 'value' : 'bar', 'path' : '/'})`
            `py.set_cookie({'name' : 'foo', 'value' : 'bar', 'path' : '/', 'secure':True})`
        """
        self.log.debug(f'py.set_cookie() - Set a cookie with name={cookie["name"]} and value={cookie["value"]}')
        self.webdriver.add_cookie(cookie)

    def execute_script(self, javascript: str, *args):
        """Executes javascript in the current window or frame.

        Args:
            javascript: The script string to execute.
            args: Any arguments to be used in the script.

        Returns:
            The value returned by the script.

        Examples:
            `py.execute_script('return document.title;')`
            `py.execute_script('return document.getElementById(arguments[0]);', element_id)`
        """
        self.log.debug("[STEP] py.execute_script() - Execute javascript into the Browser")
        return self.webdriver.execute_script(javascript, *args)

    def execute_async_script(self, javascript: str, *args):
        """Executes javascript asynchronously in the current window or frame.

        Args:
            javascript: The script string to execute.
            args: Any arguments to be used in the script.

        Returns:
            The value returned by the script.

        Examples:
            `py.execute_async_script('return document.title;')`
        """
        self.log.debug("[STEP] py.execute_async_script() - Execute javascript asynchronously into the Browser")
        return self.webdriver.execute_async_script(javascript, *args)

    def quit(self):
        """Quits the driver.

        Closes any and every associated window.
        """
        self.log.debug("py.quit() - Quit Pylenium and close all windows from the browser")
        self.webdriver.quit()

    # WINDOW #
    ##########

    @property
    def switch_to(self) -> SwitchTo:
        """Switch between contexts like Windows or Frames."""
        return SwitchTo(self)

    @property
    def window_handles(self) -> List[str]:
        """Returns the handles of all Windows in the current session."""
        return self.webdriver.window_handles

    @property
    def window_size(self) -> dict:
        """Gets the width and height of the current Window."""
        return self.webdriver.get_window_size()

    def maximize_window(self) -> "Pylenium":
        """Maximizes the current Window."""
        self.log.debug("py.maximize_window() - Maximize window")
        try:
            self.webdriver.maximize_window()
        except WebDriverException as e:
            self.log.error(f"unable to maximize window: {e.msg}")
        return self

    def set_page_load_timeout(self, timeout: int) -> "Pylenium":
        """Set the amount of time to wait for a page load to complete before throwing an error.

        Args:
            timeout: The time to wait for.
        """
        self.webdriver.set_page_load_timeout(timeout)
        return self

    def viewport(self, width: int, height: int, orientation: str = "portrait") -> "Pylenium":
        """Control the size and orientation of the current context's browser window.

        Args:
            width: The width in pixels
            height: The height in pixels
            orientation: default is 'portrait'. Pass 'landscape' to reverse the width/height.

        Examples:
            py.viewport(1280, 800) # macbook-13 size
            py.viewport(1440, 900) # macbook-15 size
            py.viewport(375, 667)  # iPhone X size
        """
        self.log.debug(
            f"[STEP] py.viewport() - Viewport set to width={width}, height={height}, orientation={orientation}"
        )
        if orientation == "portrait":
            self.webdriver.set_window_size(width, height)
        elif orientation == "landscape":
            self.webdriver.set_window_size(height, width)
        else:
            raise ValueError("Orientation must be `portrait` or `landscape`.")
        return self
