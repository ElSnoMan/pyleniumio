from typing import List

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver

from pylenium.config import PyleniumConfig
from pylenium.element import Element, Elements
from pylenium.switch_to import SwitchTo


class Pylenium:
    """ The Pylenium API.

    ## V1
        * Chrome is the default browser
        * driver executable must be in PATH
    """
    def __init__(self, config: PyleniumConfig):
        self.config = config
        self._webdriver = webdriver.Chrome()
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
    def switch_to(self) -> SwitchTo:
        """ Switch between contexts like Windows or Frames. """
        return SwitchTo(self)

    @property
    def title(self) -> str:
        """ The current page's title. """
        return self.webdriver.title

    @property
    def url(self) -> str:
        """ The current page's URL. """
        return self.webdriver.current_url

    # NAVIGATION #
    ##############

    def visit(self, url: str) -> 'Pylenium':
        """ Navigate to the given URL.

        Returns:
            `py` so you can chain another command if needed.
        """
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
        if direction == 'back':
            self.execute_script(f'window.history.go(arguments[0])', number * -1)
        elif direction == 'forward':
            self.execute_script(f'window.history.go(arguments[0])', number)
        else:
            raise ValueError(f'direction was invalid. Must be `forward` or `back` but was {direction}')

    def reload(self) -> 'Pylenium':
        """ Refreshes the current window. """
        self.webdriver.refresh()
        return self

    # FIND ELEMENTS #
    #################

    def contains(self, text: str) -> Element:
        """ Get the DOM element containing the `text`.

        Returns:
            The first element that is found, even if multiple elements match the query.
        """
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
            elements = self.wait.until(
                lambda _: self.webdriver.find_elements(By.CSS_SELECTOR, css),
                f'Could not find any elements with the CSS ``{css}``'
            )
        else:
            elements = self.webdriver.find_elements(By.CSS_SELECTOR, css)
        return Elements(self, elements)

    # Browser #
    ###########

    def delete_cookie(self, name):
        """ Deletes the cookie with the given name.

        Examples:
            `py.delete_cookie('cookie_name')`
        """
        self.webdriver.delete_cookie(name)

    def delete_all_cookies(self):
        """ Delete all cookies in the current session. """
        self.webdriver.delete_all_cookies()

    def get_cookie(self, name) -> dict:
        """ Get the cookie with the given name.

        Returns:
            The cookie if found, else None.

        Examples:
            py.get_cookie('cookie_name')
        """
        return self.webdriver.get_cookie(name)

    def get_cookies(self):
        """ Get all cookies. """
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
        return self.webdriver.execute_script(javascript, *args)

    def quit(self):
        """ Quits the driver.

        Closes any and every associated window.
        """
        self.webdriver.quit()

    # WINDOW #
    ##########

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
        if orientation == 'portrait':
            self.webdriver.set_window_size(width, height)
        elif orientation == 'landscape':
            self.webdriver.set_window_size(height, width)
        else:
            raise ValueError(f'Orientation must be `portrait` or `landscape`.')
        return self
