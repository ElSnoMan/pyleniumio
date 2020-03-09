from collections.abc import Sequence

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebElement


class Elements(Sequence):
    """ Represents a list of DOM elements. """
    def __init__(self, driver, web_elements):
        self.driver = driver
        self._current = [Element(driver, element) for element in web_elements]

    @property
    def length(self) -> int:
        """ The number of elements in the list. """
        return len(self._current)

    def pop(self, index=-1) -> 'Element':
        """ Remove and return element at index (default last).

        Args:
            index: The default is the last one, but you can specify the element by its index.

        Raises:
            IndexError if list is empty or index is out of range.
        """
        return self._current.pop(index)

    def __getitem__(self, index) -> 'Element':
        return self._current[index]

    def __len__(self) -> int:
        return self.length


class Element:
    """ Represents a DOM element. """
    def __init__(self, driver, web_element: WebElement):
        self._driver = driver
        self._element = web_element

    @property
    def current(self) -> WebElement:
        """ Gets current instance of `WebElement` that this Element is wrapped over. """
        return self._element

    @property
    def driver(self):
        """ Gets current instance of `SeleniumDriver` that found this element. """
        return self._driver

    @property
    def tag_name(self) -> str:
        """ Gets the tag name of this element. """
        return self.current.tag_name

    @property
    def text(self) -> str:
        """ Gets the InnerText of this element. """
        return self.current.text

    # METHODS #
    ###########

    def should(self):
        return Should(self)

    def get_attribute(self, attribute: str):
        """ Gets the attribute's value.

        * If the value is 'true' or 'false', then this returns a Boolean
        * If the name does not exist, then return ``None``
        * All other values are returned as strings

        Args:
            attribute: The name of the element's attribute.

        Returns:
            The value of the attribute. If the attribute does not exist, returns None
        """
        return self.current.get_attribute(attribute)

    def is_displayed(self) -> bool:
        """ Check that this element is displayed.

        Raises:
            `NoSuchElementException` if the element is not in the DOM

        Returns:
            True if element is visible to the user, else False
        """
        return self.current.is_displayed()

    # ACTIONS #
    ###########

    def clear(self) -> 'Element':
        """ Clears the text of the input or textarea element.

        * Only works on elements that can accept text entry.

        Returns:
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

        Returns:
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
        """ Gets the DOM element containing the `text`.

        Returns:
            The first, single element that is found, even if multiple elements match the query.
        """
        element = self.driver.wait.until(
            lambda _: self.current.find_element(By.XPATH, f'//*[contains(text(), "{text}")]'),
            f'Could not find element with the text ``{text}``'
        )
        return Element(self.driver, element)

    def get(self, css) -> 'Element':
        """ Gets the DOM element that matches the `css` selector in this element's context.

        Returns:
            The first, single element that is found, even if multiple elements match the query.
        """
        element = self.driver.wait.until(
            lambda _: self.current.find_element(By.CSS_SELECTOR, css),
            f'Could not find element with the CSS ``{css}``'
        )
        return Element(self._driver, element)

    def find(self, css, at_least_one=True) -> Elements:
        """ Finds all DOM elements that match the `css` selector in this element's context.

        Args:
            css: The selector
            at_least_one: True if you want to make sure at least one element is found. False can return an empty list.

        Returns:
            A list of the found elements.
        """
        if at_least_one:
            elements = self.driver.wait.until(
                lambda _: self.current.find_elements(By.CSS_SELECTOR, css),
                f'Could not find any elements with CSS ``{css}``'
            )
        else:
            elements = self.current.find_elements(By.CSS_SELECTOR, css)
        return Elements(self.driver, elements)

    def parent(self) -> 'Element':
        """ Gets the Parent element. """
        js = '''
        elem = arguments[0];
        return elem.parentNode;
        '''
        element = self.driver.current.execute_script(js, self.current)
        return Element(self.driver, element)

    def siblings(self) -> Elements:
        """ Gets the Sibling elements. """
        js = '''
        elem = arguments[0];
        var siblings = [];
        var sibling = elem.parentNode.firstChild;

        while (sibling) {
            if (sibling.nodeType === 1 && sibling !== elem) {
                siblings.push(sibling);
            }
            sibling = sibling.nextSibling
        }
        return siblings;
        '''
        elements = self.driver.current.execute_script(js, self.current)
        return Elements(self.driver, elements)


class Should:
    def __init__(self, element: Element):
        self.element = element

    def be_visible(self) -> bool:
        return self.element.is_displayed()


class And:
    def __init__(self):
        pass
