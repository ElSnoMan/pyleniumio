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
        """ Navigate to the specified URL.

        Returns
        -------
        This driver so you can chain another command if needed.
        """
        self._driver.get(url)
        return self

    # FIND ELEMENTS #
    #################

    def contains(self, text: str) -> Element:
        """ Get the DOM element containing the `text`.

        Returns
        -------
        The first, single element that is found, even if multiple elements match the query.
        """
        element = self.wait.until(lambda _: self._driver.find_element(By.XPATH, f'//*[contains(., {text})]'))
        return Element(self, element)

    def get(self, css: str) -> Element:
        """ Get the DOM element that matches the `css` selector.

        Returns
        -------
        The first, single element that is found, even if multiple elements match the query.
        """
        element = self.wait.until(lambda _: self._driver.find_element(By.CSS_SELECTOR, css))
        return Element(self, element)

    def find(self, css: str) -> Elements:
        """ Finds all DOM elements that match the `css` selector.

        Returns
        -------
        A list of the found elements.
        """
        elements = self.wait.until(
            lambda _: self.current.find_elements(By.CSS_SELECTOR, css))
        return Elements(self, elements)

    # Browser #
    ###########

    def quit(self):
        """ Quits the driver and any every associated window. """
        self.current.quit()
