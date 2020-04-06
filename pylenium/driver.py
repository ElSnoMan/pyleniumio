from typing import List, Union

import requests
from faker import Faker
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from pylenium import webdriver_factory
from pylenium.config import PyleniumConfig
from pylenium.element import Element, Elements
from pylenium.logging import Logger
from pylenium.switch_to import SwitchTo
from pylenium.wait import PyleniumWait


class PyleniumShould:
    def __init__(self, py: 'Pylenium', timeout: int, ignored_exceptions: list = None):
        self._py = py
        self._wait: PyleniumWait = self._py.wait(timeout=timeout, use_py=True, ignored_exceptions=ignored_exceptions)

    def have_title(self, title: str) -> 'Pylenium':
        """ An expectation that the title matches the given title.

        Args:
            title: The title to match.

        Returns:
            The current instance of Pylenium.

        Raises:
            `AssertionError` if the condition is not met within the timeout.
        """
        self._py.log.step('.should().have_title()', True)
        try:
            value = self._wait.until(ec.title_is(title))
        except TimeoutException:
            value = False
        if value:
            return self._py
        else:
            self._py.log.failed('.should().have_title()')
            raise AssertionError(f'Expected Title: {title}  - Actual Title: {self._py.title}')

    def contain_title(self, string: str) -> 'Pylenium':
        """ An expectation that the title contains the given string.

        Args:
            string: The case-sensitive string for the title to contain.

        Returns:
            The current instance of Pylenium.

        Raises:
            `AssertionError` if the condition is not met within the timeout.
        """
        self._py.log.step('.should().contain_title()', True)
        try:
            value = self._wait.until(ec.title_contains(string))
        except TimeoutException:
            value = False
        if value:
            return self._py
        else:
            self._py.log.failed('.should().contain_title()')
            raise AssertionError(f'Expected {string} to be in {self._py.title}')

    def have_url(self, url: str) -> 'Pylenium':
        """ An expectation that the URL matches the given url.

        Args:
            url: The url to match.

        Returns:
            The current instance of Pylenium.

        Raises:
            `AssertionError` if the condition is not met within the timeout.
        """
        self._py.log.step('.should().have_url()', True)
        try:
            value = self._wait.until(ec.url_to_be(url))
        except TimeoutException:
            value = False
        if value:
            return self._py
        else:
            self._py.log.failed('.should().have_url()')
            raise AssertionError(f'Expected URL: {url} - Actual URL: {self._py.url}')

    def contain_url(self, string: str) -> 'Pylenium':
        """ An expectation that the URL contains the given string.

        Args:
            string: The case-sensitive string for the url to contain.

        Returns:
            The current instance of Pylenium.

        Raises:
            `AssertionError` if the condition is not met within the timeout.
        """
        self._py.log.step('.should().contain_url()', True)
        try:
            value = self._wait.until(ec.url_contains(string))
        except TimeoutException:
            value = False
        if value:
            return self._py
        else:
            self._py.log.failed('.should().contain_url()', True)
            raise AssertionError(f'Expected {string} to be in {self._py.url}')


class Pylenium:
    """ The Pylenium API.

    V1
        * Chrome is the default local browser
        * Firefox is also supported
        * driver executable must be in PATH
    """
    def __init__(self, config: PyleniumConfig, logger: Logger):
        self.config = config
        self.log = logger
        self.fake = Faker()
        self.request = requests

        # Instantiate WebDriver
        self._webdriver = webdriver_factory.build_from_config(config)
        caps = self._webdriver.capabilities
        try:
            self.log.write(f'browserName: {caps["browserName"]}, browserVersion: {caps["browserVersion"]}, '
                           f'platformName: {caps["platformName"]}, session_id: {self._webdriver.session_id}')
        except:
            self.log.warning(f'webdriver.capabilities did not have a key that Pylenium was expecting. '
                             f'Is your driver executable the right version?')

        # Default instance of PyleniumWait
        self._wait = PyleniumWait(self, self._webdriver, self.config.driver.wait_time, ignored_exceptions=None)

        # Initial Browser Setup
        if config.viewport.maximize:
            self.maximize_window()
        else:
            self.viewport(config.viewport.width, config.viewport.height, config.viewport.orientation)

    @property
    def webdriver(self) -> WebDriver:
        """ The current instance of Selenium's `WebDriver` API. """
        return self._webdriver

    @property
    def title(self) -> str:
        """ The current page's title. """
        self.log.step('py.title - Get the current page title')
        return self.webdriver.title

    @property
    def url(self) -> str:
        """ The current page's URL. """
        self.log.step('py.url - Get the current page URL')
        return self.webdriver.current_url

    # NAVIGATION #
    ##############

    def visit(self, url: str) -> 'Pylenium':
        """ Navigate to the given URL.

        Returns:
            `py` so you can chain another command if needed.
        """
        self.log.step(f'py.visit() - Visit URL: ``{url}``')
        self.webdriver.get(url)
        return self

    def go(self, direction: str, number: int = 1) -> 'Pylenium':
        """ Navigate forward or back.

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
        self.log.step(f'py.go() - Go {direction} {number} in browser history')
        if direction == 'back':
            self.execute_script(f'window.history.go(arguments[0])', number * -1)
        elif direction == 'forward':
            self.execute_script(f'window.history.go(arguments[0])', number)
        else:
            raise ValueError(f'direction was invalid. Must be `forward` or `back` but was {direction}')
        return self

    def reload(self) -> 'Pylenium':
        """ Reloads the current window. """
        self.log.step('py.reload() - Reload the current page')
        self.webdriver.refresh()
        return self

    # FIND ELEMENTS #
    #################

    def contains(self, text: str, timeout: int = 0) -> Element:
        """ Get the DOM element containing the `text`.

        Args:
            text: The text for the element to contain.
            timeout: The number of seconds to wait for this to succeed. Overrides the default wait_time.

        Returns:
            The first element that is found, even if multiple elements match the query.
        """
        self.log.step(f'py.contains() - Find the element with text: ``{text}``')
        locator = (By.XPATH, f'//*[contains(text(), "{text}")]')
        element = self.wait(timeout).until(
            lambda x: x.find_element(*locator),
            f'Could not find element with the text ``{text}``'
        )
        return Element(self, element, locator)

    def get(self, css: str, timeout: int = 0) -> Element:
        """ Get the DOM element that matches the `css` selector.

        Args:
            css: The selector to use.
            timeout: The number of seconds to wait for this to succeed. Overrides the default wait_time.

        Returns:
            The first element that is found, even if multiple elements match the query.
        """
        self.log.step(f'py.get() - Find the element with css: ``{css}``')
        by = By.CSS_SELECTOR
        element = self.wait(timeout).until(
            lambda x: x.find_element(by, css),
            f'Could not find element with the CSS ``{css}``'
        )
        return Element(self, element, locator=(by, css))

    def find(self, css: str, at_least_one=True, timeout: int = 0) -> Elements:
        """ Finds all DOM elements that match the `css` selector.

        Args:
            css: The selector to use.
            at_least_one: True if you want to make sure at least one element is found. False can return an empty list.
            timeout: The number of seconds to wait for this to succeed. Overrides the default wait_time.

        Returns:
            A list of the found elements.
        """
        by = By.CSS_SELECTOR
        if at_least_one:
            self.log.step(f'py.find() - Find at least one element with css: ``{css}``')
            elements = self.wait(timeout).until(
                lambda x: x.find_elements(by, css),
                f'Could not find any elements with the CSS ``{css}``'
            )
        else:
            self.log.step(f'py.find() - Find elements with css (no wait): ``{css}``')
            elements = self.webdriver.find_elements(by, css)
        return Elements(self, elements, locator=(by, css))

    def xpath(self, xpath: str, at_least_one=True, timeout: int = 0) -> Union[Element, Elements]:
        """ Finds all DOM elements that match the `xpath` selector.

        Args:
            xpath: The selector to use.
            at_least_one: True if you want to make sure at least one element is found. False can return an empty list.
            timeout: The number of seconds to wait for this to succeed. Overrides the default wait_time.

        Returns:
            A list of the found elements. If only one is found, return that as Element.
        """
        by = By.XPATH
        if at_least_one:
            self.log.step(f'py.xpath() - Find at least one element with xpath: ``{xpath}``')
            elements = self.wait(timeout).until(
                lambda x: x.find_elements(by, xpath),
                f'Could not find any elements with the CSS ``{xpath}``'
            )
        else:
            self.log.step(f'py.xpath() - Find elements with xpath (no wait): ``{xpath}``')
            elements = self.webdriver.find_elements(by, xpath)

        if len(elements) == 1:
            self.log.info('Only 1 element matched your xpath')
            return Element(self, elements[0], locator=(by, xpath))

        self.log.info(f'{len(elements)} elements matched your xpath')
        return Elements(self, elements, locator=(by, xpath))

    # EXPECTATIONS #
    ################

    def should(self, timeout: int = 0, ignored_exceptions: list = None) -> PyleniumShould:
        """ A collection of expectations for this driver.

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

    def screenshot(self, filename: str):
        """ Take a screenshot of the current Window.

        Args:
            filename: the filepath including the filename and extension (like `.png`)

        Examples:
            py.screenshot('screenshots/home_page.png')
        """
        self.log.step(f'py.screenshot() - Save screenshot to: {filename}')
        self.webdriver.save_screenshot(filename)

    def scroll_to(self, x, y) -> 'Pylenium':
        """ Scroll to a location on the page.

        Args:
            x: The number of pixels to scroll horizontally.
            y: The number of pixels to scroll vertically.

        Examples:
            # Scroll down 500 px
            py.scroll_to(0, 500)
        """
        js = "window.scrollTo(arguments[0], arguments[1]);"
        self.webdriver.execute_script(js, x, y)
        return self

    def wait(self, timeout: int = 0, use_py: bool = False, ignored_exceptions: list = None) -> Union[WebDriverWait, PyleniumWait]:
        """ The Wait object with the given timeout in seconds.

        If timeout=0, return the default instance of wait, else return a new instance of WebDriverWait or PyleniumWait.

        Args:
            timeout: The number of seconds to wait for the condition.
            use_py: True for a PyleniumWait.
            ignored_exceptions: List of exceptions for the condition to ignore.

        Default Ignored Exceptions:
            * NoSuchElementException

        Examples:
            # use the default wait_time in pylenium.json
            py.wait().until(lambda x: x.find_element_by_id('foo').get_attribute('style') == 'display: block;')
            # use a different timeout to control how long to wait for
            py.wait(5).until(lambda x: x.find_element_by_id('foo').is_displayed())
            py.wait(15, [NoSuchElementException, WebDriverException]).until(lambda x: x.find_element_by_id('foo'))
        """
        if timeout:
            return self._wait.build(timeout, use_py, ignored_exceptions)
        else:
            return self._wait.build(self.config.driver.wait_time, use_py, ignored_exceptions)

    # BROWSER #
    ###########

    def delete_cookie(self, name):
        """ Deletes the cookie with the given name.

        Examples:
            `py.delete_cookie('cookie_name')`
        """
        self.log.info(f'py.delete_cookie() - Delete cookie named: {name}')
        self.webdriver.delete_cookie(name)

    def delete_all_cookies(self):
        """ Delete all cookies in the current session. """
        self.log.info('py.delete_all_cookies() - Delete all cookies')
        self.webdriver.delete_all_cookies()

    def get_cookie(self, name) -> dict:
        """ Get the cookie with the given name.

        Returns:
            The cookie if found, else None.

        Examples:
            py.get_cookie('cookie_name')
        """
        self.log.info(f'py.get_cookie() - Get cookie with name: {name}')
        return self.webdriver.get_cookie(name)

    def get_cookies(self):
        """ Get all cookies. """
        self.log.info('py.get_cookies() - Get all cookies')
        return self.webdriver.get_cookies()

    def set_cookie(self, cookie: dict):
        """ Adds a cookie to your current session.

        Args:
            cookie: A dictionary object, with required keys: "name" and "value";
                * optional keys: "path", "domain", "secure", "expiry"

        Examples:
            `py.set_cookie({'name' : 'foo', 'value' : 'bar'})`
            `py.set_cookie({'name' : 'foo', 'value' : 'bar', 'path' : '/'})`
            `py.set_cookie({'name' : 'foo', 'value' : 'bar', 'path' : '/', 'secure':True})`
        """
        self.log.info(f'py.set_cookie() - Set a cookie with name={cookie["name"]} and value={cookie["value"]}')
        self.webdriver.add_cookie(cookie)

    def execute_script(self, javascript: str, *args):
        """ Executes javascript in the current window or frame.

        Args:
            javascript: The script string to execute.
            args: Any arguments to be used in the script.

        Returns:
            The value returned by the script.

        Examples:
            `py.execute_script('return document.title;')`
            `py.execute_script('return document.getElementById(arguments[0]);', element_id)`
        """
        self.log.action('py.execute_script() - Execute javascript into the Browser')
        return self.webdriver.execute_script(javascript, *args)

    def quit(self):
        """ Quits the driver.

        Closes any and every associated window.
        """
        self.log.step('py.quit() - Quit Pylenium and close all windows from the browser')
        self.webdriver.quit()

    # WINDOW #
    ##########

    @property
    def switch_to(self) -> SwitchTo:
        """ Switch between contexts like Windows or Frames. """
        return SwitchTo(self)

    @property
    def window_handles(self) -> List[str]:
        """ Returns the handles of all Windows in the current session. """
        return self.webdriver.window_handles

    @property
    def window_size(self) -> dict:
        """ Gets the width and height of the current Window. """
        return self.webdriver.get_window_size()

    def maximize_window(self) -> 'Pylenium':
        """ Maximizes the current Window. """
        self.log.info('py.maximize_window() - Maximize window')
        self.webdriver.maximize_window()
        return self

    def viewport(self, width: int, height: int,  orientation: str = 'portrait') -> 'Pylenium':
        """ Control the size and orientation of the current context's browser window.

        Args:
            width: The width in pixels
            height: The height in pixels
            orientation: default is 'portrait'. Pass 'landscape' to reverse the width/height.

        Examples:
            py.viewport(1280, 800) # macbook-13 size
            py.viewport(1440, 900) # macbook-15 size
            py.viewport(375, 667)  # iPhone X size
        """
        self.log.info(f'py.viewport() - Viewport set to width={width}, height={height}, orientation={orientation}')
        if orientation == 'portrait':
            self.webdriver.set_window_size(width, height)
        elif orientation == 'landscape':
            self.webdriver.set_window_size(height, width)
        else:
            raise ValueError(f'Orientation must be `portrait` or `landscape`.')
        return self
