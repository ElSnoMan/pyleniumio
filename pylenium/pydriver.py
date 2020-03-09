from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver

from pylenium.element import Element, Elements


class SeleniumDriver:
    """ Represents a  WebDriver.

    V1
    --
    * Chrome is the default browser
    * driver executable must be in PATH
    """
    def __init__(self, wait_time: int = 10):
        self._driver = webdriver.Chrome()
        self.wait = WebDriverWait(self._driver, timeout=wait_time)

    @property
    def current(self) -> WebDriver:
        """ Current instance of `WebDriver` that this SeleniumDriver is wrapped over. """
        return self._driver

    @property
    def title(self) -> str:
        """ The current page's title. """
        return self.current.title

    def visit(self, url: str) -> 'SeleniumDriver':
        """ Navigate to the given URL.

        Returns:
            This driver so you can chain another command if needed.
        """
        self._driver.get(url)
        return self

    # FIND ELEMENTS #
    #################

    def contains(self, text: str) -> Element:
        """ Get the DOM element containing the `text`.

        Returns:
            The first, single element that is found, even if multiple elements match the query.
        """
        element = self.wait.until(
            lambda _: self._driver.find_element(By.XPATH, f'//*[contains(text(), "{text}")]'),
            f'Could not find element with the text ``{text}``'
        )
        return Element(self, element)

    def get(self, css: str) -> Element:
        """ Get the DOM element that matches the `css` selector.

        Returns:
            The first, single element that is found, even if multiple elements match the query.
        """
        element = self.wait.until(
            lambda _: self._driver.find_element(By.CSS_SELECTOR, css),
            f'Could not find element with the CSS ``{css}``'
        )
        return Element(self, element)

    def find(self, css: str, at_least_one=True) -> Elements:
        """ Finds all DOM elements that match the `css` selector.

        Args:
            css: The selector to use.
            at_least_one: True if you want to find at least one element. False can return an empty list if none are found.

        Returns:
            A list of the found elements.
        """
        if at_least_one:
            elements = self.wait.until(
                lambda _: self.current.find_elements(By.CSS_SELECTOR, css),
                f'Could not find any elements with the CSS ``{css}``'
            )
        else:
            elements = self.current.find_elements(By.CSS_SELECTOR, css)
        return Elements(self, elements)

    # Browser #
    ###########

    def execute_script(self, javascript: str, *args):
        """Executes javascript in the current window or frame.

        Args:
            javascript: The script string to execute.
            args: Any arguments to be used in the script.

        Returns:
            The value returned by the script.

        Examples:
            driver.execute_script('return document.title;')
            driver.execute_script('return document.getElementById(arguments[0]);', element_id)
        """
        return self.current.execute_script(javascript, args)

    def quit(self):
        """Quits the driver.

        Closes any and every associated window.
        """
        self.current.quit()
