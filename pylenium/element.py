from collections.abc import Sequence

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebElement


class Elements(Sequence):
    """ Represents a list of DOM elements. """
    def __init__(self, driver, web_elements):
        self.driver = driver
        self.current = [Element(driver, element) for element in web_elements]

    @property
    def is_empty(self):
        return len(self.current) == 0

    def __getitem__(self, index):
        return self.current[index]

    def __len__(self):
        return len(self.current)


class Element:
    """ Represents a DOM element. """
    def __init__(self, driver, web_element: WebElement):
        self._driver = driver
        self._element = web_element

    @property
    def current(self) -> WebElement:
        """ Current instance of `WebElement` that this Element is wrapped over. """
        return self._element

    @property
    def driver(self):
        """ Current instance of `SeleniumDriver` that found this element. """
        return self._driver

    def should(self, statement: str):
        pass

    def is_displayed(self) -> bool:
        """ Check that this element is displayed.

        Raises
        ------
        `NoSuchElementException` if the element is not in the DOM

        Returns
        -------
        True if element is visible to the user, else False
        """
        return self.current.is_displayed()

    # ACTIONS #
    ###########

    def clear(self) -> 'Element':
        """ Clears the text of the input or textarea element.

        * Only works on elements that can accept text entry.

        Returns
        -------
        This element so you can chain another command if needed.
        """
        self.current.clear()
        return self

    def click(self):
        """ Clicks the element. """
        self.current.click()

    def double_click(self):
        """ Double clicks the element. """
        ActionChains(self.driver.current).double_click(self.current)

    def hover(self) -> 'Element':
        """ Hovers the element.

        Returns
        -------
        This element so you can chain another command if needed.
        """
        ActionChains(self.driver.current).move_to_element(self.current)
        return self

    def type(self, *args) -> 'Element':
        """ Simulate a user typing keys into the input. """
        self.current.send_keys(args)
        return self

    def submit(self):
        """ Submits the form.

        * Meant for <form> elements. May not have an effect on other types.
        """
        self.current.submit()

    # FIND ELEMENTS #
    #################

    def contains(self, text) -> 'Element':
        """ Get the DOM element containing the `text`.

        Returns
        -------
        The first, single element that is found, even if multiple elements match the query.
        """
        element = self.driver.wait.until(lambda _: self.current.find_element(By.XPATH, f'//*[contains(., {text})]'))
        return Element(self.driver, element)

    def get(self, css) -> 'Element':
        """ Get the DOM element that matches the `css` selector in this element's context.

        Returns
        -------
        The first, single element that is found, even if multiple elements match the query.
        """
        element = self.driver.wait.until(lambda _: self.current.find_element(By.CSS_SELECTOR, css))
        return Element(self._driver, element)

    def find(self, css) -> Elements:
        """ Finds all DOM elements that match the `css` selector in this element's context.

        Returns
        -------
        A list of the found elements.
        """
        elements = self.driver.wait.until(lambda _: self.current.find_elements(By.CSS_SELECTOR, css))
        return Elements(self.driver, elements)


class Should:
    def __init__(self, element: Element):
        self.element = element

    def be_visible(self) -> bool:
        return self.element.is_displayed()


class And:
    def __init__(self):
        pass
