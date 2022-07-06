from logging import Logger
from typing import Dict, List, Set, Union

from faker import Faker
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from pylenium import webdriver_factory
from pylenium.a11y import PyleniumAxe
from pylenium.cdp import CDP
from pylenium.config import PyleniumConfig
from pylenium.element import Element, Elements
from pylenium.log import logger as log
from pylenium.performance import Performance
from pylenium.switch_to import SwitchTo
from pylenium.wait import PyleniumWait


class PyleniumShould:
    """A collection of conditions (aka expectations) for the Pylenium Driver including the browser, window, and more.

    Examples:
    ```
        py.should().have_title("QA at the Point")
    ```
    """

    def __init__(self, py: "Pylenium", timeout: int, ignored_exceptions: list = None):
        self._py = py
        self._wait: PyleniumWait = self._py.wait(timeout=timeout, use_py=True, ignored_exceptions=ignored_exceptions)

    def have_title(self, title: str) -> "Pylenium":
        """An expectation that the current title matches the given title.

        Args:
            title: The title to match.

        Returns:
            The current instance of Pylenium.

        Raises:
            `AssertionError` if the condition is not met within the timeout.
        """
        log.command("Pylenium.should().have_title(): `%s`", title)
        try:
            value = self._wait.until(ec.title_is(title))
        except TimeoutException:
            value = False
        if value:
            return self._py
        else:
            raise AssertionError(f"Expected Title: `{title}` - Actual Title: `{self._py.title()}`")

    def contain_title(self, string: str) -> "Pylenium":
        """An expectation that the current title contains the given string.

        Args:
            string: The case-sensitive string for the title to contain.

        Returns:
            The current instance of Pylenium.

        Raises:
            `AssertionError` if the condition is not met within the timeout.
        """
        log.command("Pylenium.should().contain_title(): `%s`", string)
        try:
            value = self._wait.until(ec.title_contains(string))
        except TimeoutException:
            value = False
        if value:
            return self._py
        else:
            raise AssertionError(f"Expected `{string}` to be in `{self._py.title()}`")

    def have_url(self, url: str) -> "Pylenium":
        """An expectation that the current URL matches the given url.

        Args:
            url: The url to match.

        Returns:
            The current instance of Pylenium.

        Raises:
            `AssertionError` if the condition is not met within the timeout.
        """
        log.command("Pylenium.should().have_url(): `%s`", url)
        try:
            value = self._wait.until(ec.url_to_be(url))
        except TimeoutException:
            value = False
        if value:
            return self._py
        else:
            raise AssertionError(f"Expected URL: `{url}` - Actual URL: `{self._py.url()}`")

    def contain_url(self, string: str) -> "Pylenium":
        """An expectation that the current URL contains the given string.

        Args:
            string: The case-sensitive string for the url to contain.

        Returns:
            The current instance of Pylenium.

        Raises:
            `AssertionError` if the condition is not met within the timeout.
        """
        log.command("Pylenium.should().contain_url(): `%s`", string)
        try:
            value = self._wait.until(ec.url_contains(string))
        except TimeoutException:
            value = False
        if value:
            return self._py
        else:
            raise AssertionError(f"Expected `{string}` to be in `{self._py.url()}`")

    def not_find(self, css: str) -> bool:
        """An expectation that there are no elements with the given CSS in the DOM.

        Args:
            css: The CSS selector.

        Returns:
            True if no elements are found.

        Raises:
            `AssertionError` if the condition is not met within the timeout.
        """
        log.command("Pylenium.should().not_find() elements with CSS: `%s`", css)
        try:
            self._wait.until_not(lambda x: x.find_element(By.CSS_SELECTOR, css))
            return True
        except TimeoutException:
            raise AssertionError(f"Found element with css: `{css}`")

    def not_findx(self, xpath: str) -> bool:
        """An expectation that there are no elements with the given XPATH in the DOM.

        Args:
            xpath: The XPATH selector.

        Returns:
            True if no elements are found.

        Raises:
            `AssertionError` if the condition is not met within the timeout.
        """
        log.command("Pylenium.should().not_findx() elements with XPATH: `%s`", xpath)
        try:
            self._wait.until_not(lambda x: x.find_element(By.XPATH, xpath))
            return True
        except TimeoutException:
            raise AssertionError(f"Found element with xpath: `{xpath}`")

    def not_contain(self, text: str) -> bool:
        """An expectation that there are no elements with the given text in the DOM.

        Args:
            text: The text to contain.

        Returns:
            True if no elements are found.

        Raises:
            `AssertionError` if the condition is not met within the timeout.
        """
        log.command("Pylenium.should().not_contain() any elements with the text: `%s`", text)
        try:
            self._wait.until_not(lambda x: x.find_element(By.XPATH, f'//*[contains(text(), "{text}")]'))
            return True
        except TimeoutException:
            raise AssertionError(f"Found element containing text: `{text}`")


class Pylenium:
    """The Pylenium API.

    Chrome is the default local browser

    Other supported browsers:
        * Firefox
        * Edge Chromium
        * IE
        * Opera
    """

    def __init__(self, config: PyleniumConfig):
        self.config = config
        self.fake = Faker()
        self.Keys = Keys
        self._webdriver = None
        self._wait = None

    def init_webdriver(self):
        """Initialize WebDriver using the Pylenium Config."""
        self._webdriver = webdriver_factory.build_from_config(self.config)
        caps = self._webdriver.capabilities
        try:
            log.debug(
                "Capabilities: browserName: %s, browserVersion: %s, platformName: %s, session_id: %s",
                caps["browserName"],
                caps["browserVersion"],
                caps["platformName"],
                self._webdriver.session_id,
            )
        except:
            log.warning(
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
    def log(self) -> Logger:
        """A simple and convenient logger to use.

        This is Pylenium's logger which can be useful, but it's recommended that you use your own.
        However, sometimes you need something simple and this logger may be enough.

        Levels:
            - CRITICAL = 50
            - ERROR    = 40
            - WARNING  = 30
            - USER     = 25 * (for YOU!)
            - INFO     = 20
            - COMMAND  = 15 * (default, used by Pylenium)
            - DEBUG    = 10

        Examples:
        ```
            # You can use the familiar debug, info, warning, error, and critical levels
            py.log.info("INFO MESSAGE")

            # Or use the custom levels (see Levels above)
            py.log.this("Hello, %s", "world")    # a message at the USER level
            py.log.command("Don't use this one") # a message at the COMMAND level
        ```

        Returns:
            Pylenium's instance of a Logger class
        """
        return log

    # region Sub APIs

    def should(self, timeout: int = 0, ignored_exceptions: list = None) -> PyleniumShould:
        """PyleniumdShould API: A collection of expectations for the current Pylenium Driver.

        Examples:
        ```
            py.should().contain_title("QA at the Point")
            py.should().have_url("https://qap.dev")
        ```
        """
        if timeout:
            wait_time = timeout
        else:
            wait_time = self.config.driver.wait_time
        return PyleniumShould(self, wait_time, ignored_exceptions)

    @property
    def axe(self) -> PyleniumAxe:
        """PyleniumAxe API: Accessibility (a11y) Auditing and Reporting.

        Examples:
        ```
            # Write automated tests against the report aXe returns!
            def test_zero_violations(py: Pylenium):
                py.visit("https://fake.website.com")
                report = py.axe.run()
                violation_count = len(report.violations)
                assert violation_count == 0, f"{violation_count} violation(s) found!"
        ```
        """
        return PyleniumAxe(self.webdriver)

    @property
    def performance(self) -> Performance:
        """Performance API: Pylenium's custom way of capturing web performnace metrics.

        Examples:
        ```
            # Store the entire WebPerformance object and log it
            perf = py.performance.get()
            log.info(perf.dict())

            # Get a single data point from WebPerformance
            tti = py.performance.get().time_to_interactive()
        ```
        """
        return Performance(self.webdriver)

    @property
    def cdp(self) -> CDP:
        """Chrome DevTools Protocol API.

        Examples:
        ```
            metrics = py.cdp.get_performance_metrics()
            >>> metrics

            {'metrics': [
                {'name': 'Timestamp', 'value': 425608.80694},
                {'name': 'AudioHandlers', 'value': 0},
                {'name': 'ThreadTime', 'value': 0.002074},
                ...
                ]
            }
        ```
        """
        return CDP(self.webdriver)

    # endregion

    # region METHODS

    def title(self) -> str:
        """Get the current page's title."""
        log.command("py.title() - Get the current page title")
        return self.webdriver.title

    def url(self) -> str:
        """Get the current page's URL."""
        log.command("py.url() - Get the current page URL")
        return self.webdriver.current_url

    # endregion

    # region NAVIGATION

    def visit(self, url: str) -> "Pylenium":
        """Navigate to the given URL.

        Returns:
            The current instance of Pylenium
        """
        log.command("py.visit() - Visit URL: `%s`", url)
        self.webdriver.get(url)
        return self

    def go(self, direction: str, number: int = 1) -> "Pylenium":
        """Navigate forward or back.

        Args:
            direction: `"forward"` or `"back"`
            number: default is 1, will go back or forward one page in history.

        Examples:
        ```
            py.go("back", 2) # will go back 2 pages in history.
            py.go("forward") # will go forward 1 page in history.
        ```

        Returns:
            The current instance of Pylenium
        """
        log.command("py.go() - Go %s %s in browser history", direction, number)
        if direction == "back":
            self.webdriver.execute_script("window.history.go(arguments[0])", number * -1)
        elif direction == "forward":
            self.webdriver.execute_script("window.history.go(arguments[0])", number)
        else:
            raise ValueError(f"direction was invalid. Must be `forward` or `back` but was {direction}")
        return self

    def reload(self) -> "Pylenium":
        """Reload (aka refresh) the current window.

        Returns:
            The current instance of Pylenium
        """
        log.command("py.reload() - Reload (refresh) the current page")
        self.webdriver.refresh()
        return self

    # endregion

    # region FIND ELEMENTS

    def contains(self, text: str, timeout: int = None) -> Element:
        """Get the DOM element containing the given text.

        * If `timeout=None` (default), use the default wait_time.
        * If `timeout > 0`, override the default wait_time.
        * If `timeout=0`, poll the DOM immediately without any waiting.

        Args:
            text: The text for the element to contain.
            timeout: The number of seconds to wait for this to succeed. Overrides the default wait_time.

        Returns:
            The first element that is found, even if multiple elements match the query.
        """
        log.command("py.contains() - Get the element containing the text: `%s`", text)
        locator = (By.XPATH, f'//*[contains(text(), "{text}")]')

        if timeout == 0:
            element = self.webdriver.find_element(*locator)
        else:
            element = self.wait(timeout).until(
                lambda x: x.find_element(*locator), f"Could not find element with the text `{text}`"
            )
        return Element(self, element, locator)

    def get(self, css: str, timeout: int = None) -> Element:
        """Get the DOM element that matches the CSS selector.

        * If `timeout=None` (default), use the default wait_time.
        * If `timeout > 0`, override the default wait_time.
        * If `timeout=0`, poll the DOM immediately without any waiting.

        Args:
            css: The selector to use.
            timeout: The number of seconds to wait for this to succeed. Overrides the default wait_time.

        Returns:
            The first element that is found, even if multiple elements match the query.
        """
        log.command("py.get() - Find the element with CSS: `%s`", css)
        by = By.CSS_SELECTOR

        if timeout == 0:
            element = self.webdriver.find_element(by, css)
        else:
            element = self.wait(timeout).until(
                lambda x: x.find_element(by, css), f"Could not find element with the CSS `{css}`"
            )
        return Element(self, element, locator=(by, css))

    def find(self, css: str, timeout: int = None) -> Elements:
        """Finds all DOM elements that match the CSS selector.

        * If `timeout=None (default)`, use the default wait_time.
        * If `timeout > 0`, override the default wait_time.
        * If `timeout=0`, poll the DOM immediately without any waiting.

        Args:
            css: The selector to use.
            timeout: The number of seconds to wait for this to succeed. Overrides the default wait_time.

        Returns:
            A list of the found elements.
        """
        by = By.CSS_SELECTOR
        log.command("py.find() - Find elements with CSS: `%s`", css)

        try:
            if timeout == 0:
                elements = self.webdriver.find_elements(by, css)
            else:
                elements = self.wait(timeout).until(
                    lambda x: x.find_elements(by, css), f"Could not find any elements with the CSS `{css}`"
                )
        except TimeoutException:
            elements = []
        return Elements(self, elements, locator=(by, css))

    def getx(self, xpath: str, timeout: int = None) -> Element:
        """Finds the DOM element that match the XPATH selector.

        * If `timeout=None` (default), use the default wait_time.
        * If `timeout > 0`, override the default wait_time.
        * If `timeout=0`, poll the DOM immediately without any waiting.

        Args:
            xpath: The selector to use.
            timeout: The number of seconds to wait for this to succeed. Overrides the default wait_time.

        Returns:
            The first element that is found, even if multiple elements match the query.
        """
        by = By.XPATH
        log.command("py.getx() - Find the element with xpath: `%s`", xpath)

        if timeout == 0:
            element = self.webdriver.find_element(by, xpath)
        else:
            element = self.wait(timeout).until(
                lambda x: x.find_element(by, xpath), f"Could not find an element with xpath: `{xpath}`"
            )
        return Element(self, element, locator=(by, xpath))

    def findx(self, xpath: str, timeout: int = None) -> Elements:
        """Finds the DOM elements that match the XPATH selector.

        * If `timeout=None` (default), use the default wait_time.
        * If `timeout > 0`, override the default wait_time.
        * If `timeout=0`, poll the DOM immediately without any waiting.

        Args:
            xpath: The selector to use.
            timeout: The number of seconds to wait for this to succeed. Overrides the default wait_time.

        Returns:
            A list of the found elements.
        """
        by = By.XPATH
        log.command("py.findx() - Find elements with xpath: `%s`", xpath)

        try:
            if timeout == 0:
                elements = self.webdriver.find_elements(by, xpath)
            else:
                elements = self.wait(timeout).until(
                    lambda x: x.find_elements(by, xpath), f"Could not find an element with xpath: `{xpath}`"
                )
        except TimeoutException:
            elements = []
        return Elements(self, elements, locator=(by, xpath))

    # endregion

    # region UTILITIES

    def wait(
        self, timeout: int = None, use_py: bool = False, ignored_exceptions: List = None
    ) -> Union[WebDriverWait, PyleniumWait]:
        """The Wait object with the given timeout in seconds.

        If `timeout=None` or `timeout=0`,
        return the default instance of wait, else return a new instance of WebDriverWait or PyleniumWait.

        Args:
            timeout: The number of seconds to wait for the condition.
            use_py: True for a PyleniumWait.
            ignored_exceptions: List of exceptions for the condition to ignore.

        Default Ignored Exceptions:
            * `NoSuchElementException`

        Examples:
        ```
            # Use the default wait_time in pylenium.json

            py.wait().until(lambda x: x.find_element(By.ID, "foo").get_attribute("style") == "display: block;")

            # Use a different timeout to control how long to wait for

            py.wait(5).until(lambda x: x.find_element(By.ID, "foo").is_displayed())
            py.wait(15, [NoSuchElementException, WebDriverException]).until(lambda x: x.find_element(By.ID, "foo"))
        ```
        """
        if timeout:  # if not None and greater than 0
            return self._wait.build(timeout, use_py, ignored_exceptions)
        else:
            return self._wait.build(self.config.driver.wait_time, use_py, ignored_exceptions)

    # endregion

    # region COOKIES

    def delete_cookie(self, name: str) -> None:
        """Deletes the cookie with the given name.

        Examples:
        ```
            py.delete_cookie("cookie_name")
        ```
        """
        log.command("py.delete_cookie() - Delete cookie named: `%s`", name)
        self.webdriver.delete_cookie(name)

    def delete_all_cookies(self) -> None:
        """Delete all cookies in the current session."""
        log.command("py.delete_all_cookies() - Delete all cookies")
        self.webdriver.delete_all_cookies()

    def get_cookie(self, name) -> Dict:
        """Get the cookie with the given name.

        Returns:
            The cookie if found, else None.

        Examples:
        ```
            cookie = py.get_cookie("cookie_name")
            assert cookie["name"] == name
        ```
        """
        log.command("py.get_cookie() - Get cookie with name: `%s`", name)
        return self.webdriver.get_cookie(name)

    def get_all_cookies(self) -> Set[Dict]:
        """Get all cookies.

        Returns:
            A set of cookies

        Examples:
        ```
            cookies = py.get_all_cookies()
            assert len(cookies) > 0
        ```
        """
        log.command("py.get_cookies() - Get all cookies")
        return self.webdriver.get_cookies()

    def set_cookie(self, cookie: Dict):
        """Adds a cookie to your current session.

        Args:
            cookie: A dictionary object, with required keys: "name" and "value";

                * optional keys: "path", "domain", "secure", "expiry"

        Examples:
        ```
            py.set_cookie({'name' : 'foo', 'value' : 'bar'})`
            py.set_cookie({'name' : 'foo', 'value' : 'bar', 'path' : '/'})
            py.set_cookie({'name' : 'foo', 'value' : 'bar', 'path' : '/', 'secure':True})
        ```
        """
        log.command("py.set_cookie() - Set a cookie with name=`%s` and value=`%s`", cookie["name"], cookie["value"])
        self.webdriver.add_cookie(cookie)

    # endregion

    # region BROWSER

    def execute_script(self, javascript: str, *args):
        """Executes javascript in the current window or frame.

        Args:
            javascript: The script string to execute.
            args: Any arguments to be used in the script.

        Returns:
            The value returned by the script.

        Examples:
        ```
            title = py.execute_script("return document.title;")
            webelement = py.execute_script("return document.getElementById(arguments[0]);", element_id)
        ```
        """
        log.command("py.execute_script() - Execute javascript into the Browser")
        return self.webdriver.execute_script(javascript, *args)

    def execute_async_script(self, javascript: str, *args):
        """Executes javascript asynchronously in the current window or frame.

        Args:
            javascript: The script string to execute.
            args: Any arguments to be used in the script.

        Returns:
            The value returned by the script.

        Examples:
        ```
            py.execute_async_script("return document.title;")
        ```
        """
        log.command("py.execute_async_script() - Execute javascript asynchronously into the Browser")
        return self.webdriver.execute_async_script(javascript, *args)

    def quit(self):
        """Quits the driver.

        Closes any and every window/tab associated with the current session.
        """
        log.command("py.quit() - Quit Pylenium and close all windows from the browser session")
        self.webdriver.quit()

    def screenshot(self, filename: str) -> str:
        """Take a screenshot of the current Window.

        Args:
            filename: the filepath including the filename and extension (like `.png`)

        Examples:
        ```
            py.screenshot("screenshots/home_page.png")
        ```
        """
        log.command("py.screenshot() - Save screenshot to: `%s`}", filename)
        self.webdriver.save_screenshot(filename)
        return filename

    def scroll_to(self, x, y) -> "Pylenium":
        """Scroll to a location on the page.

        Args:
            x: The number of pixels to scroll horizontally.
            y: The number of pixels to scroll vertically.

        Examples:
        ```
            # Scroll down 500 px
            py.scroll_to(0, 500)
        ```
        """
        log.command("py.scroll_to() - Scroll to (%s, %s)", x, y)
        js = "window.scrollTo(arguments[0], arguments[1]);"
        self.webdriver.execute_script(js, x, y)
        return self

    @property
    def switch_to(self) -> SwitchTo:
        """Switch between contexts like Windows, Tabs, and iFrames.

        Examples:
        ```
            py.switch_to.new_tab()
            py.switch_to.frame("iframe-id")
        ```
        """
        return SwitchTo(self)

    def maximize_window(self) -> "Pylenium":
        """Maximizes the current Window."""
        try:
            self.webdriver.maximize_window()
        except WebDriverException as e:
            log.error(f"Unable to maximize window: {e.msg}")
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
        ```
            py.viewport(1280, 800) # macbook-13 size
            py.viewport(1440, 900) # macbook-15 size
            py.viewport(375, 667)  # iPhone X size
        ```
        """
        log.command("py.viewport() - Set viewport to width=%s, height=%s, orientation=%s", width, height, orientation)
        if orientation == "portrait":
            self.webdriver.set_window_size(width, height)
        elif orientation == "landscape":
            self.webdriver.set_window_size(height, width)
        else:
            raise ValueError("Orientation must be `portrait` or `landscape`.")
        return self

    @property
    def window_handles(self) -> List[str]:
        """Returns the handles of all Windows in the current session.

        * This property is mainly used to switch between windows or tabs

        Examples:
        ```
            # assert that there are two windows - the main website and a new tab
            windows = py.window_handles
            assert len(windows) == 2

            # then switch to the new tab
            py.switch_to.window(name_or_handle=windows[1])
        ```
        """
        return self.webdriver.window_handles

    @property
    def window_size(self) -> Dict:
        """Gets the width and height of the current Window.

        Examples:
        ```
            size = py.window_size
            print(size["width"])
            print(size["height"])
        ```
        """
        return self.webdriver.get_window_size()
