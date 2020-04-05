import time
from typing import List, Union, Tuple, Optional

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as ec


class ElementWait:
    def __init__(self, webelement, timeout: int, ignored_exceptions: list = None):
        self._webelement = webelement
        self._timeout = 10 if timeout == 0 else timeout
        if ignored_exceptions:
            self._ignored_exceptions = ignored_exceptions
        else:
            self._ignored_exceptions = (
                NoSuchElementException
            )

    def until(self, method, message=''):
        screen = None
        stacktrace = None

        end_time = time.time() + self._timeout
        while True:
            try:
                value = method(self._webelement)
                if value:
                    return value
            except self._ignored_exceptions as exc:
                screen = getattr(exc, 'screen', None)
                stacktrace = getattr(exc, 'stacktrace', None)
            time.sleep(0.5)
            if time.time() > end_time:
                break
        raise TimeoutException(message, screen, stacktrace)


class ElementShould:
    """ Expectations for the current element that is already in the DOM. """
    def __init__(self, py, element: 'Element', timeout: int, ignored_exceptions: list = None):
        self._py = py
        self._element = element
        self._wait = ElementWait(element.webelement, timeout, ignored_exceptions)

    # POSITIVE CONDITIONS #
    #######################

    def be_clickable(self) -> 'Element':
        """ An expectation that the element is displayed and enabled so you can click it.

        Returns:
            The current element.

        Raises:
            `AssertionError` if the condition is not met in the specified amount of time.
        """
        self._py.log.step('.should().be_clickable()', True)
        try:
            value = self._wait.until(lambda e: e.is_displayed() and e.is_enabled())
        except TimeoutException:
            value = False
        if value:
            return self._element
        else:
            self._py.log.failed('.should().be_clickable()')
            raise AssertionError('Element was not clickable')

    def be_checked(self) -> 'Element':
        """ An expectation that the element is checked.

        Returns:
            The current element.

        Raises:
            `AssertionError` if the condition is not met in the specified amount of time.
        """
        self._py.log.step('.should().be_checked()', True)
        try:
            value = self._wait.until(lambda e: self._element.is_checked())
        except TimeoutException:
            value = False
        if value:
            return self._element
        else:
            self._py.log.failed('.should().be_checked()')
            raise AssertionError('Element was not checked')

    def be_disabled(self) -> 'Element':
        """ An expectation that the element is disabled.

        Returns:
            The current element.

        Raises:
            `AssertionError` if the condition is not met in the specified amount of time.
        """
        self._py.log.step('.should().be_disabled()', True)
        try:
            value = self._wait.until(lambda e: not e.is_enabled())
        except TimeoutException:
            value = False
        if value:
            return self._element
        else:
            self._py.log.failed('.should().be_disabled()')
            raise AssertionError('Element was not disabled')

    def be_enabled(self) -> 'Element':
        """ An expectation that the element is enabled.

        Returns:
            The current element.

        Raises:
            `AssertionError` if the condition is not met in the specified amount of time.
        """
        self._py.log.step('.should().be_enabled()', True)
        try:
            value = self._wait.until(lambda e: e.is_enabled())
        except TimeoutException:
            value = False
        if value:
            return self._element
        else:
            self._py.log.failed('.should().be_enabled()')
            raise AssertionError('Element was not enabled')

    def be_focused(self) -> 'Element':
        """ An expectation that the element is focused.

        Returns:
            The current element.

        Raises:
            `AssertionError` if the condition is not met in the specified amount of time.
        """
        self._py.log.step('.should().be_focused()', True)
        try:
            value = self._wait.until(lambda e: e == self._py.webdriver.switch_to.active_element)
        except TimeoutException:
            value = False

        if value:
            return self._element
        else:
            self._py.log.failed('.should().be_focused()')
            raise AssertionError('Element did not have focus')

    def be_hidden(self) -> 'Element':
        """ An expectation that the element is not displayed but still in the DOM (aka hidden).

        Returns:
            The current element.

        Raises:
            `AssertionError` if the condition is not met in the specified amount of time.
        """
        self._py.log.step('.should().be_hidden()', True)
        try:
            value = self._wait.until(lambda e: e and not e.is_displayed())
        except TimeoutException:
            value = False

        if value:
            return self._element
        else:
            self._py.log.failed('.should().be_hidden()')
            raise AssertionError('Element was not hidden')

    def be_selected(self) -> 'Element':
        """ An expectation that the element is selected.

        Returns:
            The current element.

        Raises:
            `AssertionError` if the condition is not met in the specified amount of time.
        """
        self._py.log.step('.should().be_selected()', True)
        try:
            value = self._wait.until(lambda e: e.is_selected())
        except TimeoutException:
            value = False

        if value:
            return self._element
        else:
            self._py.log.failed('.should().be_selected()')
            raise AssertionError('Element was not selected')

    def be_visible(self) -> 'Element':
        """ An expectation that the element is displayed.

        Returns:
            The current element.

        Raises:
            `AssertionError` if the condition is not met in the specified amount of time.
        """
        self._py.log.step('.should().be_visible()', True)
        try:
            value = self._wait.until(lambda e: e and e.is_displayed())
        except TimeoutException:
            value = False

        if value:
            return self._element
        else:
            self._py.log.failed('.should().be_visible()')
            raise AssertionError('Element was not visible')

    def have_attr(self, attr: str, value: str) -> 'Element':
        """ An expectation that the element has the given attribute with the given value.

        Args:
            attr: The name of the attribute.
            value: The value of the attribute.

        Returns:
            The current element.

        Raises:
            `AssertionError` if the condition is not met in the specified amount of time.
        """
        self._py.log.step('.should().have_attr()', True)
        try:
            val = self._wait.until(lambda e: e.get_attribute(attr) == value)
        except TimeoutException:
            val = False

        if val:
            return self._element
        else:
            self._py.log.failed('.should().have_attr()')
            raise AssertionError(f'Element did not have attribute ``{attr}`` with the value of ``{value}``')

    def have_class(self, class_name: str) -> 'Element':
        """ An expectation that the element has the given className.

        Args:
            class_name: The `.className` of the element

        Returns:
            The current element.

        Raises:
            `AssertionError` if the condition is not met in the specified amount of time.
        """
        self._py.log.step('.should().have_class()', True)
        try:
            val = self._wait.until(lambda e: e.get_attribute('class') == class_name)
        except TimeoutException:
            val = False

        if val:
            return self._element
        else:
            self._py.log.failed('.should().have_class()')
            raise AssertionError(f'Element did not have className ``{class_name}``')

    def have_prop(self, prop: str, value: str) -> 'Element':
        """ An expectation that the element has the given property with the given value.

        Args:
            prop: The name of the property.
            value: The value of the property.

        Returns:
            The current element.

        Raises:
            `AssertionError` if the condition is not met in the specified amount of time.
        """
        self._py.log.step('.should().have_prop()', True)
        try:
            val = self._wait.until(lambda e: e.get_property(property) == value)
        except TimeoutException:
            val = False

        if val:
            return self._element
        else:
            self._py.log.failed('.should().have_prop()')
            raise AssertionError(f'Element did not have property ``{prop}`` with the value of ``{value}``')

    def have_text(self, text, case_sensitive=True) -> 'Element':
        """ An expectation that the element has the given text.

        Args:
            text: The exact text to match.
            case_sensitive: False if you want to ignore casing and leading/trailing spaces.

        Returns:
            The current element.

        Raises:
            `AssertionError` if the condition is not met in the specified amount of time.
        """
        self._py.log.step('.should().have_text()', True)
        try:
            if case_sensitive:
                value = self._wait.until(lambda e: e.text == text)
            else:
                value = self._wait.until(lambda e: e.text.strip().lower() == text.lower())
        except TimeoutException:
            value = False

        if value:
            return self._element
        else:
            self._py.log.failed('.should().have_text()')
            raise AssertionError(f'Element did not have text matching ``{text}``')

    def contain_text(self, text, case_sensitive=True) -> 'Element':
        """ An expectation that the element contains the given text.

        Args:
            text: The text that the element should contain.
            case_sensitive: False if you want to ignore casing and leading/trailing spaces.

        Returns:
            The current element.

        Raises:
            `AssertionError` if the condition is not met in the specified amount of time.
        """
        self._py.log.step('.should().contain_text()', True)
        try:
            if case_sensitive:
                value = self._wait.until(lambda e: text in e.text)
            else:
                value = self._wait.until(lambda e: text.lower() in e.text.strip().lower())
        except TimeoutException:
            value = False

        if value:
            return self._element
        else:
            self._py.log.failed('.should().contain_text()')
            raise AssertionError(f'Element did not contain the text ``{text}``')

    def have_value(self, value) -> 'Element':
        """ An expectation that the element has the given value.

        Args:
            value: The exact value to match. Pass `None` if you expect the element not to have the value attribute.

        Returns:
            The current element.

        Raises:
            `AssertionError` if the condition is not met in the specified amount of time.

        Examples:
            * An element with no `value` attribute will yield `None`
            * An element with a `value` attribute with no value will yield an empty string `""`
            * An element with a `value` attribute with a value will yield the value
        """
        self._py.log.step('.should().have_value()', True)
        try:
            val = self._wait.until(lambda e: e.get_attribute('value') == value)
        except TimeoutException:
            val = False

        if val:
            return self._element
        else:
            self._py.log.failed('.should().have_value()')
            raise AssertionError(f'Element did not have value matching ``{value}``')

    # NEGATIVE CONDITIONS #
    #######################

    def not_be_focused(self) -> 'Element':
        """ An expectation that the element is not focused.

        Returns:
            The current element.

        Raises:
            `AssertionError` if the condition is not met in the specified amount of time.
        """
        self._py.log.step('.should().not_be_focused()', True)
        try:
            value = self._wait.until(lambda e: e != self._py.webdriver.switch_to.active_element)
        except TimeoutException:
            value = False

        if value:
            return self._element
        else:
            self._py.log.failed('.should().not_be_focused()')
            raise AssertionError('Element had focus')

    def not_exist(self) -> 'Pylenium':
        """ An expectation that the element no longer exists in the DOM.

        Returns:
            The current element.

        Raises:
            `AssertionError` if the condition is not met in the specified amount of time.

        Examples:
            # wait for a loading spinner to appear and then disappear once the load is complete
            py.get(#spinner).should().not_exist()
        """
        self._py.log.step('.should().not_exist()', True)
        try:
            value = self._wait.until(ec.invisibility_of_element(self._element.webelement))
        except TimeoutException:
            value = False
        if value:
            return self._py
        else:
            self._py.log.failed('.should().not_exist()')
            raise AssertionError('Element was still visible or still in the DOM')

    def not_have_attr(self, attr: str, value: str) -> 'Element':
        """ An expectation that the element does not have the given attribute with the given value.

        Either the attribute does not exist on the element or the value does not match the given value.

        Args:
            attr: The name of the attribute.
            value: The value of the attribute.

        Returns:
            The current element.

        Raises:
            `AssertionError` if the condition is not met in the specified amount of time.
        """
        self._py.log.step('.should().not_have_attr()', True)
        try:
            val = self._wait.until(lambda e: e.get_attribute(attr) is None or e.get_attribute(attr) != value)
        except TimeoutException:
            val = False

        if val:
            return self._element
        else:
            self._py.log.failed('.should().not_have_attr()')
            raise AssertionError(f'Element still had attribute ``{attr}`` with the value of ``{value}``')

    def not_have_value(self, value) -> 'Element':
        """ An expectation that the element does not have the given value.

        Args:
            value: The exact value not to match. Pass `None` if you expect the element to have the value attribute.

        Returns:
            The current element.

        Raises:
            `AssertionError` if the condition is not met in the specified amount of time.

        Examples:
            * An element with no `value` attribute will yield `None`
            * An element with a `value` attribute with no value will yield an empty string `""`
            * An element with a `value` attribute with a value will yield the value
        """
        self._py.log.step('.should().not_have_value()', True)
        try:
            val = self._wait.until(lambda e: e.get_attribute('value') != value)
        except TimeoutException:
            val = False

        if val:
            return self._element
        else:
            self._py.log.failed('.should().not_have_value()')
            raise AssertionError(f'Element had value matching ``{value}``')

    def not_have_text(self, text, case_sensitive=True) -> 'Element':
        """ An expectation that the element does not have the given text.

        Args:
            text: The exact text to match.
            case_sensitive: False if you want to ignore casing and leading/trailing spaces.

        Returns:
            The current element.

        Raises:
            `AssertionError` if the condition is not met in the specified amount of time.
        """
        self._py.log.step('.should().not_have_text()', True)
        try:
            if case_sensitive:
                value = self._wait.until(lambda e: e.text != text)
            else:
                value = self._wait.until(lambda e: e.text.strip().lower() != text.lower())
        except TimeoutException:
            value = False

        if value:
            return self._element
        else:
            self._py.log.failed('.should().not_have_text()')
            raise AssertionError(f'Element had the text matching ``{text}``')


class Elements(List['Element']):
    """ Represents a list of DOM elements. """
    def __init__(self, py, web_elements, locator: Optional[Tuple]):
        self._list = [Element(py, element, None) for element in web_elements]
        self._py = py
        self.locator = locator
        super().__init__(self._list)

    @property
    def length(self) -> int:
        """ The number of elements in the list. """
        return len(self._list)

    def is_empty(self) -> bool:
        """ Checks if there are no elements in the list. """
        return self.length == 0

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
        self._py.log.action('elements.check() - Check all checkboxes or radio buttons in this list', True)
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
        self._py.log.action('elements.uncheck() - Uncheck all checkboxes or radio buttons in this list', True)
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
    def __init__(self, py, web_element: WebElement, locator: Optional[Tuple]):
        self._py = py
        self._webelement = web_element,
        self.locator = locator

    @property
    def webelement(self) -> WebElement:
        """ The current instance of the Selenium's `WebElement` API. """
        if isinstance(self._webelement, Tuple):
            return self._webelement[0]
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

    # EXPECTATIONS #
    ################

    def should(self, timeout: int = 0, ignored_exceptions: list = None) -> ElementShould:
        """ A collection of expectations for this element.

        Examples:
            py.get('#foo').should().be_clickable()
        """
        if timeout:
            wait_time = timeout
        else:
            wait_time = self._py.config.driver.wait_time
        return ElementShould(self.py, self, wait_time, ignored_exceptions)

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

    def get_property(self, property: str):
        """ Gets the property's value.

        Args:
            property: The name of the element's property.

        Returns:
            The value of the attribute.
        """
        self.py.log.step(f'.get_property() - Get the {property} value of this element', True)
        return self.webelement.get_property(property)

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

    def is_enabled(self) -> bool:
        """ Check that this element is enabled.

        Returns:
            True if the element is enabled, else False
        """
        self.py.log.step('Check if this element is enabled', True)
        return self.webelement.is_enabled()

    def is_selected(self) -> bool:
        """ Check that this element is selected.

        Returns:
            True if the element is selected, else False
        """
        self.py.log.step('Check if this element is selected', True)
        return self.webelement.is_selected()

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

    def click(self, force=False) -> 'Pylenium':
        """ Clicks the element.

        Args:
            force: If True, a JavascriptExecutor command is sent instead of Selenium's native `.click()`.

        Returns:
            The current instance of Pylenium so you can chain another command.
        """
        self.py.log.action('.click() - Click this element', True)
        if force:
            self.py.webdriver.execute_script('arguments[0].click()', self.webelement)
        else:
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
            value: The value, text content or index of the `<option>` to be selected.

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
        except BaseException:
            Select(self.webelement).select_by_index(value)
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
        locator = (By.XPATH, f'.//*[contains(text(), "{text}")]')
        element = self.py.wait(timeout).until(
            lambda _: self.webelement.find_element(*locator),
            f'Could not find element with the text ``{text}``'
        )
        return Element(self.py, element, locator)

    def get(self, css: str, timeout: int = 0) -> 'Element':
        """ Gets the DOM element that matches the `css` selector in this element's context.

        Args:
            css: The selector
            timeout: The number of seconds to find the element.

        Returns:
            The first element that is found, even if multiple elements match the query.
        """
        self.py.log.step(f'.get() - Find the element that has css: ``{css}``', True)
        by = By.CSS_SELECTOR
        element = self.py.wait(timeout).until(
            lambda _: self.webelement.find_element(by, css),
            f'Could not find element with the CSS ``{css}``'
        )
        return Element(self.py, element, locator=(by, css))

    def find(self, css: str, at_least_one=True, timeout: int = 0) -> Elements:
        """ Finds all DOM elements that match the `css` selector in this element's context.

        Args:
            css: The selector
            at_least_one: True if you want to make sure at least one element is found. False can return an empty list.
            timeout: The number of seconds to find at least one element.

        Returns:
            A list of the found elements.
        """
        by = By.CSS_SELECTOR
        if at_least_one:
            self.py.log.step(f'.find() - Find at least one element with css: ``{css}``', True)
            elements = self.py.wait(timeout).until(
                lambda _: self.webelement.find_elements(by, css),
                f'Could not find any elements with CSS ``{css}``'
            )
        else:
            self.py.log.step(f'.find() - Find elements with css (no wait): ``{css}``', True)
            elements = self.webelement.find_elements(by, css)
        return Elements(self.py, elements, locator=(by, css))

    def xpath(self, xpath: str, at_least_one=True, timeout: int = 0) -> Union['Element', Elements]:
        """ Finds all DOM elements that match the `xpath` selector.

        Args:
            xpath: The selector to use.
            at_least_one: True if you want to make sure at least one element is found. False can return an empty list.
            timeout: The number of seconds to find at least one element.

        Returns:
            A list of the found elements. If only one is found, return that as Element.
        """
        by = By.XPATH
        if at_least_one:
            self.py.log.step(f'.xpath() - Find at least one element with xpath: ``{xpath}``', True)
            elements = self.py.wait(timeout).until(
                lambda _: self.webelement.find_elements(by, xpath),
                f'Could not find any elements with the xpath ``{xpath}``'
            )
        else:
            self.py.log.step(f'.xpath() - Find elements with xpath (no wait): ``{xpath}``', True)
            elements = self.webelement.find_elements(by, xpath)

        if len(elements) == 1:
            # If only one is found, return the single Element
            return Element(self, elements[0], locator=(by, xpath))

        return Elements(self, elements, locator=(by, xpath))

    def children(self) -> Elements:
        """ Gets the Child elements. """
        self.py.log.info('.children() - Get the children of this element', True)
        elements = self.py.webdriver.execute_script('return arguments[0].children;', self.webelement)
        return Elements(self.py, elements, None)

    def parent(self) -> 'Element':
        """ Gets the Parent element. """
        self.py.log.info('.parent() - Get the parent of this element', True)
        js = '''
        elem = arguments[0];
        return elem.parentNode;
        '''
        element = self.py.webdriver.execute_script(js, self.webelement)
        return Element(self.py, element, None)

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
        return Elements(self.py, elements, None)

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
