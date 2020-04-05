import time
from typing import Tuple, Optional, Union

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from pylenium.element import Element, Elements


class PyleniumWait:
    """ The Pylenium version of Wait that returns Element and Elements objects."""
    def __init__(self, py, webdriver, timeout, ignored_exceptions: Optional[Tuple] = None):
        self._py = py
        self._webdriver = webdriver
        self._wait = WebDriverWait(
            driver=webdriver,
            timeout=timeout,
            ignored_exceptions=ignored_exceptions
        )

    def sleep(self, seconds: int):
        """ The test will sleep for the given number of seconds.

        Args:
            seconds: The number of seconds to sleep for.

        This is the same as using time.sleep()
        """
        time.sleep(seconds)

    def until(self, method, message=''):
        """ Wait until the method returns a non-False value.

        * The method uses Selenium WebDriver

        Args:
            method: The condition to wait for
            message: The message to show if the condition is not met in the time frame.

        Returns:
            If the value is a webelement, return a Pylenium Element object
            If the value is a list of WebElement, return a Pylenium Elements object
            Else return the non-False value

        Examples:
            # return an Element
            py.wait().until(lambda x: x.find_element_by_id('foo'), 'element "foo" was not found')
            # return Elements
            py.wait().until(lambda x: x.find_elements_by_xpath('//a'))
            # return True
            py.wait(5).until(lambda x: x.title  == 'QA at the Point')
        """
        value = self._wait.until(method, message)
        if isinstance(value, WebElement):
            return Element(self._py, value, None)
        if isinstance(value, list):
            try:
                return Elements(self._py, value, None)
            except:
                pass  # not a list of WebElement
        return value

    def build(self, timeout: int, use_py=False, ignored_exceptions: list = None) -> Union[WebDriverWait, 'PyleniumWait']:
        """ Builds a WebDriverWait or PyleniumWait.

        Args:
            timeout: The number of seconds to wait for the condition to be True
            use_py: True if you want a PyleniumWait. False for a default WebDriverWait
            ignored_exceptions: List of exceptions to ignore in the Wait

        Returns:
            New instance of WebDriverWait if use_pylenium=False, else returns PyleniumWait
        """
        if use_py:
            return PyleniumWait(self._py, self._webdriver, timeout, ignored_exceptions)
        else:
            return WebDriverWait(self._webdriver, timeout, ignored_exceptions=ignored_exceptions)
