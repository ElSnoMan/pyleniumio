from typing import List, Union, Optional

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver

from pylenium.config import PyleniumConfig
from pylenium.element import Element, Elements
from pylenium.logging import Logger
from pylenium.switch_to import SwitchTo


class WebDriverFactory:
    """ Factory to build WebDrivers. """
    def __init__(self, config: Optional[PyleniumConfig]):
        self.config = config

    def build_from_config(self) -> WebDriver:
        """ Build a WebDriver using pylenium.json. """
        if self.config.driver.remote_url:
            return self.build_remote(
                browser=self.config.driver.browser,
                remote_url=self.config.driver.remote_url
            )
        else:
            return self.build_chrome()

    def build_chrome(self) -> WebDriver:
        """ Build a ChromeDriver. """
        return webdriver.Chrome()

    def build_remote(self, browser: str, remote_url: str) -> WebDriver:
        """ Build a RemoteDriver connected to a Grid.

        Args:
            browser: Name of the browser to connect to.
            remote_url: The URL to connect to the Grid.

        Returns:
            The instance of WebDriver once the connection is successful
        """
        if browser == 'firefox':
            caps = webdriver.DesiredCapabilities.FIREFOX
        elif browser == 'edge':
            caps = webdriver.DesiredCapabilities.EDGE
        elif browser == 'ie':
            caps = webdriver.DesiredCapabilities.INTERNETEXPLORER
        elif browser == 'safari':
            caps = webdriver.DesiredCapabilities.SAFARI
        else:  # default to chrome
            caps = webdriver.DesiredCapabilities.CHROME

        return webdriver.Remote(
            command_executor=remote_url,
            desired_capabilities=caps
        )


class Pylenium:
    """ The Pylenium API.

    ## V1
        * Chrome is the default local browser
        * chromedriver executable must be in PATH
    """
    def __init__(self, config: PyleniumConfig, logger: Logger):
        self.config = config
        self.log = logger

        # Instantiate WebDriver
        self._webdriver = WebDriverFactory(config).build_from_config()
        caps = self._webdriver.capabilities
        self.log.write(f'browserName: {caps["browserName"]}, browserVersion: {caps["browserVersion"]}, platformName: {caps["platformName"]}, session_id: {self._webdriver.session_id}')

        # Initial Browser Setup
        self.wait = WebDriverWait(self._webdriver, timeout=config.driver.wait_time)
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
        self.log.step(f'py.visit() - Visit URL: {url}')
        self.webdriver.get(url)
        return self

    def go(self, direction: str, number: int = 1):
        """ Navigate forward or back.

        This command executes `window.history.go(number)`

        Args:
            direction: 'forward' or 'back'
            number: default is 1, will go back or forward one page in history.

        Examples:
            `py.go('back', 2)` will go back 2 pages in history.
            `py.go('forward')` will go forward 1 page in history.
        """
        self.log.step(f'py.go() - Go {direction} {number} in browser history')
        if direction == 'back':
            self.execute_script(f'window.history.go(arguments[0])', number * -1)
        elif direction == 'forward':
            self.execute_script(f'window.history.go(arguments[0])', number)
        else:
            raise ValueError(f'direction was invalid. Must be `forward` or `back` but was {direction}')

    def reload(self) -> 'Pylenium':
        """ Refreshes the current window. """
        self.log.step('py.reload() - Refresh the current page')
        self.webdriver.refresh()
        return self

    # FIND ELEMENTS #
    #################

    def contains(self, text: str) -> Element:
        """ Get the DOM element containing the `text`.

        Returns:
            The first element that is found, even if multiple elements match the query.
        """
        self.log.step(f'py.contains() - Find the element with text: ``{text}``')
        element = self.wait.until(
            lambda _: self._webdriver.find_element(By.XPATH, f'//*[contains(text(), "{text}")]'),
            f'Could not find element with the text ``{text}``'
        )
        return Element(self, element)

    def get(self, css: str) -> Element:
        """ Get the DOM element that matches the `css` selector.

        Returns:
            The first element that is found, even if multiple elements match the query.
        """
        self.log.step(f'py.get() - Find the element with css: ``{css}``')
        element = self.wait.until(
            lambda _: self._webdriver.find_element(By.CSS_SELECTOR, css),
            f'Could not find element with the CSS ``{css}``'
        )
        return Element(self, element)

    def find(self, css: str, at_least_one=True) -> Elements:
        """ Finds all DOM elements that match the `css` selector.

        Args:
            css: The selector to use.
            at_least_one: True if you want to make sure at least one element is found. False can return an empty list.

        Returns:
            A list of the found elements.
        """
        if at_least_one:
            self.log.step(f'py.find() - Find at least one element with css: ``{css}``')
            elements = self.wait.until(
                lambda _: self.webdriver.find_elements(By.CSS_SELECTOR, css),
                f'Could not find any elements with the CSS ``{css}``'
            )
        else:
            self.log.action(f'py.find() - Find elements with css (no wait): ``{css}``')
            elements = self.webdriver.find_elements(By.CSS_SELECTOR, css)
        return Elements(self, elements)

    def xpath(self, xpath: str, at_least_one=True) -> Union[Element, Elements]:
        """ Finds all DOM elements that match the `xpath` selector.

        Args:
            xpath: The selector to use.
            at_least_one: True if you want to make sure at least one element is found. False can return an empty list.

        Returns:
            A list of the found elements. If only one is found, return that as Element.
        """
        if at_least_one:
            self.log.step(f'py.xpath() - Find at least one element with xpath: ``{xpath}``')
            elements = self.wait.until(
                lambda _: self.webdriver.find_elements(By.XPATH, xpath),
                f'Could not find any elements with the CSS ``{xpath}``'
            )
        else:
            self.log.step(f'py.xpath() - Find elements with xpath (no wait): ``{xpath}``')
            elements = self.webdriver.find_elements(By.CSS_SELECTOR, xpath)

        if len(elements) == 1:
            self.log.info('Only 1 element matched your xpath')
            return Element(self, elements[0])

        self.log.info(f'{len(elements)} elements matched your xpath')
        return Elements(self, elements)

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
