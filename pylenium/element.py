from typing import List, Union

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.support.select import Select


class Elements(List['Element']):
    """ Represents a list of DOM elements. """
    def __init__(self, py, web_elements):
        self._list = [Element(py, element) for element in web_elements]
        self.py = py
        super().__init__(self._list)

    @property
    def length(self) -> int:
        """ The number of elements in the list. """
        return len(self._list)

    def first(self) -> 'Element':
        """ Gets the first element in the list.

        Raises:
            `IndexError` if the list is empty.
        """
        if self.length > 0:
            return self._list[0]
        else:
            raise IndexError('Cannot get first() from an empty list.')

    def last(self) -> 'Element':
        """ Gets the last element in the list.

        Raises:
            `IndexError` if the list is empty.
        """
        if self.length > 0:
            return self._list[-1]
        else:
            raise IndexError('Cannot get last() from an empty list.')

    # ACTIONS #
    ###########

    def check(self, allow_selected=False) -> 'Elements':
        """ Check all checkboxes or radio buttons in this list.

        Args:
            allow_selected: Do not raise error if any elements are already selected.

        Raises:
            `ValueError` if any elements are already selected.
            `ValueError` if any elements are not checkboxes or radio buttons.
        """
        self.py.log.action('elements.check() - Check all checkboxes or radio buttons in this list', True)
        for element in self._list:
            element.check(allow_selected)
        return self

    def uncheck(self, allow_deselected=False) -> 'Elements':
        """ Check all checkboxes or radio buttons in this list.

        Args:
            allow_deselected: Do not raise error if any elements are already deselected.

        Raises
            `ValueError` if any elements are already selected.
            `ValueError` if any elements are not checkboxes or radio buttons.
        """
        self.py.log.action('elements.uncheck() - Uncheck all checkboxes or radio buttons in this list', True)
        for element in self._list:
            element.uncheck(allow_deselected)
        return self

    # CONDITIONS #
    ##############

    def are_checked(self) -> bool:
        """ Check that all checkbox or radio buttons in this list are selected. """
        for element in self._list:
            if not element.is_checked():
                return False
        # every element is checked
        return True


class Element:
    """ Represents a DOM element. """
    def __init__(self, py, web_element: WebElement):
        self._py = py
        self._webelement = web_element

    @property
    def webelement(self) -> WebElement:
        """ The current instance of the Selenium's `WebElement` API. """
        return self._webelement

    @property
    def py(self):
        """ The current instance of `py` that found this element. """
        return self._py

    @property
    def tag_name(self) -> str:
        """ Gets the tag name of this element. """
        self.py.log.step('.tag_name - Get the tag name of this element', True)
        return self.webelement.tag_name

    @property
    def text(self) -> str:
        """ Gets the InnerText of this element. """
        self.py.log.step('.text - Get the text in this element', True)
        return self.webelement.text

    # METHODS #
    ###########

    def get_attribute(self, attribute: str):
        """ Gets the attribute's value.

            * If the value is 'true' or 'false', then this returns a Boolean
            * If the name does not exist, then return None
            * All other values are returned as strings

        Args:
            attribute: The name of the element's attribute.

        Returns:
            The value of the attribute. If the attribute does not exist, returns None
        """
        self.py.log.step(f'.get_attribute() - Get the {attribute} value of this element', True)
        value = self.webelement.get_attribute(attribute)
        if value == 'true':
            return True
        elif value == 'false':
            return False
        else:
            return value

    # CONDITIONS #
    ##############

    def is_checked(self) -> bool:
        """ Check that this checkbox or radio button is selected.

        Raises:
            `ValueError` if element is not a checkbox or radio button
        """
        type_ = self.webelement.get_attribute('type')
        if type_ != 'checkbox' or type_ == 'radio':
            raise ValueError('Element is not a checkbox or radio button.')

        self.py.log.step(f'Check if this checkbox or radio button element is checked', True)
        return self.py.execute_script('return arguments[0].checked;', self.webelement)

    def is_displayed(self) -> bool:
        """ Check that this element is displayed.

        Raises:
            `NoSuchElementException` if the element is not in the DOM

        Returns:
            True if element is visible to the user, else False
        """
        self.py.log.step('Check if this element is displayed', True)
        return self.webelement.is_displayed()

    # ACTIONS #
    ###########

    def check(self, allow_selected=False) -> 'Element':
        """ Check this checkbox or radio button.

        Args:
            allow_selected: Do not raise error if element is already selected.

        Raises:
            `ValueError` if element is already selected.
            `ValueError` if element is not a checkbox or radio button

        Returns:
            This element so you can chain another command.
        """
        self.py.log.action('.check() - Select this checkbox or radio button', True)
        type_ = self.webelement.get_attribute('type')
        if type_ == 'checkbox' or type_ == 'radio':
            checked = self.py.webdriver.execute_script('return arguments[0].checked;', self.webelement)
            if not checked:
                self.webelement.click()
                return self
            elif allow_selected:
                return self
            else:
                raise ValueError(f'{type_} is already selected.')
        raise ValueError('Element is not a checkbox or radio button.')

    def uncheck(self, allow_deselected=False) -> 'Element':
        """ Uncheck this checkbox or radio button.

        Args:
            allow_deselected: Do not raise error if element is already deselected.

        Raises:
            `ValueError` if element is already deselected.
            `ValueError` if element is not a checkbox or radio button

        Returns:
            This element so you can chain another command.
        """
        self.py.log.action('.uncheck() - Deselect this checkbox or radio button', True)
        type_ = self.webelement.get_attribute('type')
        if type_ == 'checkbox' or type_ == 'radio':
            checked = self.py.webdriver.execute_script('return arguments[0].checked;', self.webelement)
            if checked:
                self.webelement.click()
                return self
            elif allow_deselected:
                return self
            else:
                raise ValueError(f'{type_} is already deselected.')
        raise ValueError('Element is not a checkbox or radio button.')

    def clear(self) -> 'Element':
        """ Clears the text of the input or textarea element.

            * Only works on elements that can accept text entry.

        Returns:
            This element so you can chain another command.
        """
        self.py.log.action('.clear() - Clear the input of this element', True)
        self.webelement.clear()
        return self

    def click(self) -> 'Pylenium':
        """ Clicks the element.

        Returns:
            The current instance of Pylenium so you can chain another command.
        """
        self.py.log.action('.click() - Click this element', True)
        self.webelement.click()
        return self.py

    def deselect(self, value) -> 'Pylenium':
        """ Deselects an `<option>` within a multi `<select>` element.

        Args:
            value: The value or text content of the `<option>` to be deselected.

        Raises:
            `ValueError` if this element is not a `<select>`

        Returns:
            The current instance of Pylenium so you can chain another command.
        """
        self.py.log.action('.deselect() - Deselect this element', True)
        if self.webelement.tag_name != 'select':
            raise ValueError(f'Can only perform Deselect on <select> elements. Tag name: {self.webelement.tag_name}')

        select = Select(self.webelement)
        if not select.is_multiple:
            raise NotImplementedError(f'Deselect can only be performed on multi-select elements.')

        try:
            select.deselect_by_visible_text(value)
        except NoSuchElementException:
            select.deselect_by_value(value)
        finally:
            return self.py

    def double_click(self) -> 'Pylenium':
        """ Double clicks the element.

        Returns:
            The current instance of Pylenium so you can chain another command.
        """
        self.py.log.action('.double_click() - Double click this element', True)
        ActionChains(self.py.webdriver).double_click(self.webelement).perform()
        return self.py

    def hover(self) -> 'Pylenium':
        """ Hovers the element.

        Returns:
            The current instance of Pylenium so you can chain another command.
        """
        self.py.log.action('.hover() - Hovers this element', True)
        ActionChains(self.py.webdriver).move_to_element(self.webelement).perform()
        return self.py

    def right_click(self) -> 'Pylenium':
        """ Right clicks the element.

        Returns:
            The current instance of Pylenium so you can chain another command.
        """
        self.py.log.step('.right_click() - Right click this element', True)
        ActionChains(self.py.webdriver).context_click(self.webelement).perform()
        return self.py

    def select(self, value) -> 'Element':
        """ Selects an `<option>` within a `<select>` element.

        Args:
            value: The value or text content of the `<option>` to be selected.

        Raises:
            `ValueError` if this element is not a `<select>`.

        Returns:
            This element so you can chain another command if needed.
        """
        self.py.log.action('.select() - Select an option in this element', True)
        if self.webelement.tag_name != 'select':
            raise ValueError(f'Can only perform Select on <select> elements. Current tag name: {self.webelement.tag_name}')
        try:
            Select(self.webelement).select_by_visible_text(value)
        except NoSuchElementException:
            Select(self.webelement).select_by_value(value)
        finally:
            return self

    def select_many(self, values: list) -> 'Pylenium':
        """ Selects multiple `<options>` within a `<select>` element.

        Args:
            values: The list of values or text contents of the `<option>` to be selected.

        Raises:
            `ValueError` if this element is not a `<select>`.

        Returns:
            The current instance of Pylenium so you can chain another command.
        """
        self.py.log.action('.select_many() - Select many options in this element', True)
        if self.webelement.tag_name != 'select':
            raise ValueError(f'Can only perform Select on <select> elements. Current tag name: {self.webelement.tag_name}')

        select = Select(self.webelement)
        if not select.is_multiple:
            raise NotImplementedError(f'This <select> only allows a single option. Use .select() instead.')

        try:
            for val in values:
                select.select_by_visible_text(val)
        except NoSuchElementException:
            for val in values:
                select.select_by_value(val)
        finally:
            return self.py

    def submit(self) -> 'Pylenium':
        """ Submits the form.

            * Meant for <form> elements. May not have an effect on other types.

        Returns:
            The current instance of Pylenium so you can chain another command.
        """
        self.py.log.action('.submit() - Submit the form', True)
        self.webelement.submit()
        return self.py

    def type(self, *args) -> 'Element':
        """ Simulate a user typing keys into the input.

        Returns:
            This element so you can chain another command.
        """
        self.py.log.action('.type() - Type keys into this element', True)
        self.webelement.send_keys(args)
        return self

    # FIND ELEMENTS #
    #################

    def contains(self, text: str, timeout: int = 0) -> 'Element':
        """ Gets the DOM element containing the `text`.

        Args:
            text: The text for the element to contain
            timeout: The number of seconds to find the element.

        Returns:
            The first element that is found, even if multiple elements match the query.
        """
        self.py.log.step(f'.contains() - Find the element that contains text: ``{text}``', True)
        element = self.py.wait(timeout).until(
            lambda _: self.webelement.find_element(By.XPATH, f'//*[contains(text(), "{text}")]'),
            f'Could not find element with the text ``{text}``'
        )
        return Element(self.py, element)

    def get(self, css: str, timeout: int = 0) -> 'Element':
        """ Gets the DOM element that matches the `css` selector in this element's context.

        Args:
            css: The selector
            timeout: The number of seconds to find the element.

        Returns:
            The first element that is found, even if multiple elements match the query.
        """
        self.py.log.step(f'.get() - Find the element that has css: ``{css}``', True)
        element = self.py.wait(timeout).until(
            lambda _: self.webelement.find_element(By.CSS_SELECTOR, css),
            f'Could not find element with the CSS ``{css}``'
        )
        return Element(self.py, element)

    def find(self, css: str, at_least_one=True, timeout: int = 0) -> Elements:
        """ Finds all DOM elements that match the `css` selector in this element's context.

        Args:
            css: The selector
            at_least_one: True if you want to make sure at least one element is found. False can return an empty list.
            timeout: The number of seconds to find at least one element.

        Returns:
            A list of the found elements.
        """
        self.py.log.step(f'.find() - Find the elements with css: ``{css}``', True)
        if at_least_one:
            elements = self.py.wait(timeout).until(
                lambda _: self.webelement.find_elements(By.CSS_SELECTOR, css),
                f'Could not find any elements with CSS ``{css}``'
            )
        else:
            elements = self.webelement.find_elements(By.CSS_SELECTOR, css)
        return Elements(self.py, elements)

    def xpath(self, xpath: str, at_least_one=True, timeout: int = 0) -> Union['Element', Elements]:
        """ Finds all DOM elements that match the `xpath` selector.

        Args:
            xpath: The selector to use.
            at_least_one: True if you want to make sure at least one element is found. False can return an empty list.
            timeout: The number of seconds to find at least one element.

        Returns:
            A list of the found elements. If only one is found, return that as Element.
        """
        self.py.log.step(f'.xpath() - Find the elements with xpath: ``{xpath}``', True)
        if at_least_one:
            elements = self.py.wait(timeout).until(
                lambda _: self.webelement.find_elements(By.XPATH, xpath),
                f'Could not find any elements with the CSS ``{xpath}``'
            )
        else:
            elements = self.webelement.find_elements(By.CSS_SELECTOR, xpath)

        if len(elements) == 1:
            # If only one is found, return the single Element
            return Element(self, elements[0])

        return Elements(self, elements)

    def children(self) -> Elements:
        """ Gets the Child elements. """
        self.py.log.info('.children() - Get the children of this element', True)
        elements = self.py.webdriver.execute_script('return arguments[0].children;', self.webelement)
        return Elements(self.py, elements)

    def parent(self) -> 'Element':
        """ Gets the Parent element. """
        self.py.log.info('.parent() - Get the parent of this element', True)
        js = '''
        elem = arguments[0];
        return elem.parentNode;
        '''
        element = self.py.webdriver.execute_script(js, self.webelement)
        return Element(self.py, element)

    def siblings(self) -> Elements:
        """ Gets the Sibling elements. """
        self.py.log.info('.siblings() - Get the siblings of this element', True)
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
        elements = self.py.webdriver.execute_script(js, self.webelement)
        return Elements(self.py, elements)

    # UTILITIES #
    #############

    def screenshot(self, filename) -> 'Element':
        """ Take a screenshot of the current element.

        Args:
            filename: the filepath including the filename and extension (like `.png`)

        Examples:
            py.get('#save-button').screenshot('elements/save-button.png')
        """
        self.py.log.info(f'.screenshot() - Take a screenshot and save to: {filename}', True)
        self.webelement.screenshot(filename)
        return self

    def scroll_into_view(self) -> 'Element':
        """ Scroll this element into view. """
        self.py.log.info(f'.scroll_into_view() - Scroll this element into view', True)
        self.py.webdriver.execute_script('arguments[0].scrollIntoView(true);', self.webelement)
        return self
