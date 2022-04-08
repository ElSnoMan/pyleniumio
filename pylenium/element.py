from pylenium import jquery
import time
from typing import List, Tuple, Optional

from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
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
            self._ignored_exceptions = NoSuchElementException

    def until(self, method, message=""):
        screen = None
        stacktrace = None

        end_time = time.time() + self._timeout
        while True:
            try:
                value = method(self._webelement)
                if value:
                    return value
            except self._ignored_exceptions as exc:
                screen = getattr(exc, "screen", None)
                stacktrace = getattr(exc, "stacktrace", None)
            time.sleep(0.5)
            if time.time() > end_time:
                break
        raise TimeoutException(message, screen, stacktrace)


class ElementsShould:
    """Expectations for the current list of elements, if any."""

    def __init__(self, py, elements: "Elements", timeout: int, ignored_exceptions: list = None):
        self._py = py
        self._elements = elements
        self._wait = py.wait(timeout=timeout, use_py=True, ignored_exceptions=ignored_exceptions)

    def be_empty(self) -> bool:
        """An expectation that the list has no elements.

        Returns:
            True if empty, else False.

        Raises:
            `AssertionError` if the condition is not met in the specified amount of time.
        """
        self._py.log.debug("\t[ASSERT] .should().be_empty()")
        try:
            if self._elements.is_empty():
                return True
            else:
                locator = self._elements.locator
                value = self._wait.until(lambda drvr: len(drvr.find_elements(*locator)) == 0)
        except TimeoutException:
            value = False
        if value:
            return True
        else:
            self._py.log.critical(".should().be_empty()")
            raise AssertionError("List of elements was not empty.")

    def be_greater_than(self, length: int) -> bool:
        """An expectation that the number of elements in the list is greater than the given length.

        Args:
            length: The length that the list should be greater than.

        Raises:
            `AssertionError` if the condition is not met in the specified amount of time.
        """
        self._py.log.debug(f"  [ASSERT] .should().be_greater_than() ``{length}``")
        try:
            if self._elements.length() > length:
                return True
            else:
                locator = self._elements.locator
                value = self._wait.until(lambda drvr: len(drvr.find_elements(*locator)) > length)
        except TimeoutException:
            value = False
        if value:
            return True
        else:
            self._py.log.critical(".should().be_greater_than()")
            raise AssertionError(f"Length of elements was not greater than {length}.")

    def be_less_than(self, length: int) -> bool:
        """An expectation that the number of elements in the list is less than the given length.

        Args:
            length: The length that the list should be less than.

        Raises:
            `AssertionError` if the condition is not met in the specified amount of time.
        """
        self._py.log.debug(f"\t[ASSERT] .should().be_less_than() ``{length}``")
        try:
            if self._elements.length() < length:
                return True
            else:
                locator = self._elements.locator
                value = self._wait.until(lambda drvr: len(drvr.find_elements(*locator)) < length)
        except TimeoutException:
            value = False
        if value:
            return True
        else:
            self._py.log.critical(".should().be_less_than()")
            raise AssertionError(f"Length of elements was not less than {length}.")

    def have_length(self, length: int) -> bool:
        """An expectation that the number of elements in the list is equal to the given length.

        Args:
            length: The length that the list should be equal to.

        Raises:
            `AssertionError` if the condition is not met in the specified amount of time.
        """
        self._py.log.debug(f"\t[ASSERT] .should().have_length() ``{length}``")
        try:
            if self._elements.length() == length:
                return True
            else:
                locator = self._elements.locator
                value = self._wait.until(lambda drvr: len(drvr.find_elements(*locator)) == length)
        except TimeoutException:
            value = False
        if value:
            return True
        else:
            self._py.log.critical(".should().have_length()")
            raise AssertionError(f"Length of elements was not equal to {length}.")

    def not_be_empty(self) -> "Elements":
        """An expectation that the list has at least one element.

        Returns:
            The list of elements if not empty.

        Raises:
            `AssertionError` if the condition is not met in the specified amount of time.
        """
        self._py.log.debug("\t[ASSERT] .should().not_be_empty()")
        try:
            if not self._elements.is_empty():
                return self._elements
            else:
                locator = self._elements.locator
                value = self._wait.until(lambda drvr: drvr.find_elements(*locator))
        except TimeoutException:
            value = False
        if value:
            return Elements(self._py, value, self._elements.locator)
        else:
            self._py.log.critical(".should().not_be_empty()")
            raise AssertionError("List of elements was empty.")


class ElementShould:
    """Expectations for the current element that is already in the DOM."""

    def __init__(self, py, element: "Element", timeout: int, ignored_exceptions: list = None):
        self._py = py
        self._element = element
        self._wait = ElementWait(element.webelement, timeout, ignored_exceptions)

    # region POSITIVE CONDITIONS

    def be_clickable(self) -> "Element":
        """An expectation that the element is displayed and enabled so you can click it.

        Returns:
            The current element.

        Raises:
            `AssertionError` if the condition is not met in the specified amount of time.
        """
        self._py.log.debug("\t[ASSERT] .should().be_clickable()")
        try:
            value = self._wait.until(lambda e: e.is_displayed() and e.is_enabled())
        except TimeoutException:
            value = False
        if value:
            return self._element
        else:
            self._py.log.critical(".should().be_clickable()")
            raise AssertionError("Element was not clickable")

    def be_checked(self) -> "Element":
        """An expectation that the element is checked.

        Returns:
            The current element.

        Raises:
            `AssertionError` if the condition is not met in the specified amount of time.
        """
        self._py.log.debug("\t[ASSERT] .should().be_checked()")
        try:
            value = self._wait.until(lambda e: self._element.is_checked())
        except TimeoutException:
            value = False
        if value:
            return self._element
        else:
            self._py.log.critical(".should().be_checked()")
            raise AssertionError("Element was not checked")

    def be_disabled(self) -> "Element":
        """An expectation that the element is disabled.

        Returns:
            The current element.

        Raises:
            `AssertionError` if the condition is not met in the specified amount of time.
        """
        self._py.log.debug("\t[ASSERT] .should().be_disabled()")
        try:
            value = self._wait.until(lambda e: not e.is_enabled())
        except TimeoutException:
            value = False
        if value:
            return self._element
        else:
            self._py.log.critical(".should().be_disabled()")
            raise AssertionError("Element was not disabled")

    def be_enabled(self) -> "Element":
        """An expectation that the element is enabled.

        Returns:
            The current element.

        Raises:
            `AssertionError` if the condition is not met in the specified amount of time.
        """
        self._py.log.debug("\t[ASSERT] .should().be_enabled()")
        try:
            value = self._wait.until(lambda e: e.is_enabled())
        except TimeoutException:
            value = False
        if value:
            return self._element
        else:
            self._py.log.critical(".should().be_enabled()")
            raise AssertionError("Element was not enabled")

    def be_focused(self) -> "Element":
        """An expectation that the element is focused.

        Returns:
            The current element.

        Raises:
            `AssertionError` if the condition is not met in the specified amount of time.
        """
        self._py.log.debug("\t[ASSERT] .should().be_focused()")
        try:
            value = self._wait.until(lambda e: e == self._py.webdriver.switch_to.active_element)
        except TimeoutException:
            value = False

        if value:
            return self._element
        else:
            self._py.log.critical(".should().be_focused()")
            raise AssertionError("Element was not focused")

    def be_hidden(self) -> "Element":
        """An expectation that the element is not displayed but still in the DOM (aka hidden).

        Returns:
            The current element.

        Raises:
            `AssertionError` if the condition is not met in the specified amount of time.
        """
        self._py.log.debug("\t[ASSERT] .should().be_hidden()")
        try:
            value = self._wait.until(lambda e: e and not e.is_displayed())
        except TimeoutException:
            value = False

        if value:
            return self._element
        else:
            self._py.log.critical(".should().be_hidden()")
            raise AssertionError("Element was not hidden")

    def be_selected(self) -> "Element":
        """An expectation that the element is selected.

        Returns:
            The current element.

        Raises:
            `AssertionError` if the condition is not met in the specified amount of time.
        """
        self._py.log.debug("\t[ASSERT] .should().be_selected()")
        try:
            value = self._wait.until(lambda e: e.is_selected())
        except TimeoutException:
            value = False

        if value:
            return self._element
        else:
            self._py.log.critical(".should().be_selected()")
            raise AssertionError("Element was not selected")

    def be_visible(self) -> "Element":
        """An expectation that the element is displayed.

        Returns:
            The current element.

        Raises:
            `AssertionError` if the condition is not met in the specified amount of time.
        """
        self._py.log.debug("\t[ASSERT] .should().be_visible()")
        try:
            value = self._wait.until(lambda e: e and e.is_displayed())
        except TimeoutException:
            value = False

        if value:
            return self._element
        else:
            self._py.log.critical(".should().be_visible()")
            raise AssertionError("Element was not visible")

    def have_attr(self, attr: str, value: Optional[str] = None) -> "Element":
        """An expectation that the element has the given attribute with the given value.

        Args:
            attr: The name of the attribute.
            value (optional): The value of the attribute.

        Returns:
            The current element.

        Raises:
            `AssertionError` if the condition is not met in the specified amount of time.
        """
        self._py.log.debug(f"\t[ASSERT] .should().have_attr() ``{attr}``")
        try:
            if value is None:
                val = self._wait.until(lambda e: e.get_attribute(attr))
            else:
                val = self._wait.until(lambda e: e.get_attribute(attr) == value)
        except TimeoutException:
            val = False

        if val:
            return self._element
        else:
            self._py.log.critical(".should().have_attr()")
            if value is None:
                raise AssertionError(f"Element did not have attribute: ``{attr}``")
            else:
                raise AssertionError(
                    f"Expected Attribute Value: ``{value}`` "
                    f'- Actual Attribute Value: ``{self._element.get_attribute("value")}``'
                )

    def have_class(self, class_name: str) -> "Element":
        """An expectation that the element has the given className.

        Args:
            class_name: The `.className` of the element

        Returns:
            The current element.

        Raises:
            `AssertionError` if the condition is not met in the specified amount of time.
        """
        self._py.log.debug(f"\t[ASSERT] .should().have_class() ``{class_name}``")
        try:
            val = self._wait.until(lambda e: e.get_attribute("class") == class_name)
        except TimeoutException:
            val = False

        if val:
            return self._element
        else:
            self._py.log.critical(".should().have_class()")
            raise AssertionError(
                f"Expected className: ``{class_name}`` "
                f'- Actual className: ``{self._element.get_attribute("class")}``'
            )

    def have_prop(self, prop: str, value: str) -> "Element":
        """An expectation that the element has the given property with the given value.

        Args:
            prop: The name of the property.
            value: The value of the property.

        Returns:
            The current element.

        Raises:
            `AssertionError` if the condition is not met in the specified amount of time.
        """
        self._py.log.debug(f"\t[ASSERT] .should().have_prop() ``{prop}`` with value of ``{value}``")
        try:
            val = self._wait.until(lambda e: e.get_property(prop) == value)
        except TimeoutException:
            val = False

        if val:
            return self._element
        else:
            self._py.log.critical(".should().have_prop()")
            raise AssertionError(
                f"Expected Property value: ``{value}`` "
                f"- Actual Property value: ``{self._element.get_property(prop)}``"
            )

    def have_text(self, text, case_sensitive=True) -> "Element":
        """An expectation that the element has the given text.

        Args:
            text: The exact text to match.
            case_sensitive: False if you want to ignore casing and leading/trailing spaces.

        Returns:
            The current element.

        Raises:
            `AssertionError` if the condition is not met in the specified amount of time.
        """
        self._py.log.debug(f"\t[ASSERT] .should().have_text() ``{text}``")
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
            self._py.log.critical(".should().have_text()")
            raise AssertionError(f"Expected text: ``{text}`` - Actual text: ``{self._element.text()}``")

    def contain_text(self, text, case_sensitive=True) -> "Element":
        """An expectation that the element contains the given text.

        Args:
            text: The text that the element should contain.
            case_sensitive: False if you want to ignore casing and leading/trailing spaces.

        Returns:
            The current element.

        Raises:
            `AssertionError` if the condition is not met in the specified amount of time.
        """
        self._py.log.debug(f"\t[ASSERT] .should().contain_text() ``{text}``")
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
            self._py.log.critical(".should().contain_text()")
            raise AssertionError(f"Expected ``{text}`` to be in ``{self._element.text()}``")

    def have_value(self, value) -> "Element":
        """An expectation that the element has the given value.

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
        self._py.log.debug(f"\t[ASSERT] .should().have_value() ``{value}``")
        try:
            val = self._wait.until(lambda e: e.get_attribute("value") == value)
        except TimeoutException:
            val = False

        if val:
            return self._element
        else:
            self._py.log.critical(".should().have_value()")
            raise AssertionError(
                f"Expected value: ``{value}`` " f'- Actual value: ``{self._element.get_attribute("value")}``'
            )

    # endregion

    # region NEGATIVE CONDITIONS

    def not_be_focused(self) -> "Element":
        """An expectation that the element is not focused.

        Returns:
            The current element.

        Raises:
            `AssertionError` if the condition is not met in the specified amount of time.
        """
        self._py.log.debug("\t[ASSERT] .should().not_be_focused()")
        try:
            value = self._wait.until(lambda e: e != self._py.webdriver.switch_to.active_element)
        except TimeoutException:
            value = False

        if value:
            return self._element
        else:
            self._py.log.critical(".should().not_be_focused()")
            raise AssertionError("Element had focus")

    def disappear(self):
        """An expectation that the element eventually disappears from the DOM.

        Returns:
            The current instance of Pylenium.

        Raises:
            `AssertionError` if the condition is not met in the specified amount of time.

        Examples:
            # wait for a loading spinner to appear and then disappear once the load is complete
            py.get(#spinner).should().disappear()
        """
        self._py.log.debug("\t[ASSERT] .should().disappear()")
        try:
            value = self._wait.until(ec.invisibility_of_element(self._element.webelement))
        except TimeoutException:
            value = False
        if value:
            return self._py
        else:
            self._py.log.critical(".should().disappear()")
            raise AssertionError("Element was still visible or still in the DOM")

    def not_have_attr(self, attr: str, value: Optional[str] = None) -> "Element":
        """An expectation that the element does not have the given attribute with the given value.

        Either the attribute does not exist on the element or the value does not match the given value.

        Args:
            attr: The name of the attribute.
            value (optional): The value of the attribute.

        Returns:
            The current element.

        Raises:
            `AssertionError` if the condition is not met in the specified amount of time.
        """
        self._py.log.debug(f"\t[ASSERT] .should().not_have_attr() ``{attr}``")
        try:
            if value is None:
                val = self._wait.until(lambda e: not e.get_attribute(attr))
            else:
                val = self._wait.until(lambda e: e.get_attribute(attr) is None or e.get_attribute(attr) != value)
        except TimeoutException:
            val = False

        if val:
            return self._element
        else:
            self._py.log.critical(".should().not_have_attr()")
            if value is None:
                raise AssertionError(f"Element had the attribute: ``{attr}``")
            else:
                raise AssertionError(f"Element still had attribute ``{attr}`` with the value of ``{value}``")

    def not_have_value(self, value) -> "Element":
        """An expectation that the element does not have the given value.

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
        self._py.log.debug(f"\t[ASSERT] .should().not_have_value() ``{value}``")
        try:
            val = self._wait.until(lambda e: e.get_attribute("value") != value)
        except TimeoutException:
            val = False

        if val:
            return self._element
        else:
            self._py.log.critical(".should().not_have_value()")
            raise AssertionError(f"Element had value matching ``{value}``")

    def not_have_text(self, text, case_sensitive=True) -> "Element":
        """An expectation that the element does not have the given text.

        Args:
            text: The exact text to match.
            case_sensitive: False if you want to ignore casing and leading/trailing spaces.

        Returns:
            The current element.

        Raises:
            `AssertionError` if the condition is not met in the specified amount of time.
        """
        self._py.log.debug(f"\t[ASSERT] .should().not_have_text() ``{text}``")
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
            self._py.log.critical(".should().not_have_text()")
            raise AssertionError(f"Element had the text matching ``{text}``")

    # endregion


class Elements(List["Element"]):
    """Represents a list of DOM elements."""

    def __init__(self, py, web_elements, locator: Optional[Tuple]):
        self._list = [Element(py, element, None) for element in web_elements]
        self._py = py
        self.locator = locator
        super().__init__(self._list)

    def should(self, timeout: int = 0, ignored_exceptions: list = None) -> ElementsShould:
        """A collection of expectations for this list of elements.

        Examples:
            py.find('option').should().not_be_empty()
        """
        if timeout:
            wait_time = timeout
        else:
            wait_time = self._py.config.driver.wait_time
        return ElementsShould(self._py, self, wait_time, ignored_exceptions)

    def length(self) -> int:
        """The number of elements in the list."""
        return len(self._list)

    def is_empty(self) -> bool:
        """Checks if there are no elements in the list."""
        return self.length() == 0

    def first(self) -> "Element":
        """Gets the first element in the list.

        Raises:
            `IndexError` if the list is empty.
        """
        if self.length() > 0:
            return self._list[0]
        else:
            raise IndexError("Cannot get first() from an empty list.")

    def last(self) -> "Element":
        """Gets the last element in the list.

        Raises:
            `IndexError` if the list is empty.
        """
        if self.length() > 0:
            return self._list[-1]
        else:
            raise IndexError("Cannot get last() from an empty list.")

    # ACTIONS #
    ###########

    def check(self, allow_selected=False) -> "Elements":
        """Check all checkboxes or radio buttons in this list.

        Args:
            allow_selected: Do not raise error if any elements are already selected.

        Raises:
            `ValueError` if any elements are already selected.
            `ValueError` if any elements are not checkboxes or radio buttons.
        """
        self._py.log.debug("\t[STEP] elements.check() - Check all checkboxes or radio buttons in this list")
        for element in self._list:
            element.check(allow_selected)
        return self

    def uncheck(self, allow_deselected=False) -> "Elements":
        """Check all checkboxes or radio buttons in this list.

        Args:
            allow_deselected: Do not raise error if any elements are already deselected.

        Raises
            `ValueError` if any elements are already selected.
            `ValueError` if any elements are not checkboxes or radio buttons.
        """
        self._py.log.debug("\t[STEP] elements.uncheck() - Uncheck all checkboxes or radio buttons in this list")
        for element in self._list:
            element.uncheck(allow_deselected)
        return self

    # CONDITIONS #
    ##############

    def are_checked(self) -> bool:
        """Check that all checkbox or radio buttons in this list are selected."""
        for element in self._list:
            if not element.is_checked():
                return False
        # every element is checked
        return True


class Element:
    """Represents a DOM element."""

    def __init__(self, py, web_element: WebElement, locator: Optional[Tuple]):
        self._py = py
        self._webelement = (web_element,)
        self.locator = locator

    @property
    def webelement(self) -> WebElement:
        """The current instance of the Selenium's `WebElement` API."""
        if isinstance(self._webelement, Tuple):
            return self._webelement[0]
        return self._webelement

    @property
    def py(self):
        """The current instance of `py` that found this element."""
        return self._py

    def css_value(self, property_name: str):
        """Gets the CSS Value of this element given the css_name."""
        self.py.log.debug(f"\t[STEP] .css_value() - Get a CSS Value given the property: ``{property_name}``")
        try:
            return self.webelement.value_of_css_property(property_name)
        except WebDriverException:
            self.py.log.warning(f"Property Name: ``{property_name}`` is invalid or not found.")
            return None

    def tag_name(self) -> str:
        """Gets the tag name of this element."""
        tag_name = self.webelement.tag_name
        self.py.log.debug(f"\t[STEP] .tag_name() - Get the tag name of this element ``{tag_name}``")
        return tag_name

    def text(self) -> str:
        """Gets the InnerText of this element."""
        text = self.webelement.text
        self.py.log.debug(f"\t[STEP] .text() - Get the text of this element ``{text}``")
        return text

    # EXPECTATIONS #
    ################

    def should(self, timeout: int = 0, ignored_exceptions: list = None) -> ElementShould:
        """A collection of expectations for this element.

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
        """Gets the attribute's value.

            * If the value is 'true' or 'false', then this returns a Boolean
            * If the name does not exist, then return None
            * All other values are returned as strings

        Args:
            attribute: The name of the element's attribute.

        Returns:
            The value of the attribute. If the attribute does not exist, returns None
        """
        self.py.log.debug(f"\t[STEP] .get_attribute() - Get the ``{attribute}`` value of this element")
        value = self.webelement.get_attribute(attribute)
        if value == "true":
            return True
        elif value == "false":
            return False
        else:
            return value

    def get_property(self, prop: str):
        """Gets the property's value.

        Args:
            prop: The name of the element's property.

        Returns:
            The value of the attribute.
        """
        self.py.log.debug(f"\t[STEP] .get_property() - Get the ``{prop}`` value of this element")
        return self.webelement.get_property(prop)

    # CONDITIONS #
    ##############

    def is_checked(self) -> bool:
        """Check that this checkbox or radio button is selected.

        Raises:
            `ValueError` if element is not a checkbox or radio button
        """
        type_ = self.webelement.get_attribute("type")
        if type_ != "checkbox" and type_ != "radio":
            raise ValueError("Element is not a checkbox or radio button.")

        self.py.log.debug("\t[STEP] Check if this checkbox or radio button element is checked")
        return self.py.execute_script("return arguments[0].checked;", self.webelement)

    def is_displayed(self) -> bool:
        """Check that this element is displayed.

        Raises:
            `NoSuchElementException` if the element is not in the DOM

        Returns:
            True if element is visible to the user, else False
        """
        self.py.log.debug("\t[STEP] Check if this element is displayed")
        return self.webelement.is_displayed()

    def is_enabled(self) -> bool:
        """Check that this element is enabled.

        Returns:
            True if the element is enabled, else False
        """
        self.py.log.debug("\t[STEP] Check if this element is enabled")
        return self.webelement.is_enabled()

    def is_selected(self) -> bool:
        """Check that this element is selected.

        Returns:
            True if the element is selected, else False
        """
        self.py.log.debug("\t[STEP] Check if this element is selected")
        return self.webelement.is_selected()

    # ACTIONS #
    ###########

    def check(self, allow_selected=False) -> "Element":
        """Check this checkbox or radio button.

        Args:
            allow_selected: Do not raise error if element is already selected.

        Raises:
            `ValueError` if element is already selected.
            `ValueError` if element is not a checkbox or radio button

        Returns:
            This element so you can chain another command.
        """
        self.py.log.debug("\t[STEP] .check() - Select this checkbox or radio button")
        type_ = self.webelement.get_attribute("type")
        if type_ == "checkbox" or type_ == "radio":
            checked = self.py.webdriver.execute_script("return arguments[0].checked;", self.webelement)
            if not checked:
                self.webelement.click()
                return self
            elif allow_selected:
                return self
            else:
                raise ValueError(f"{type_} is already selected.")
        raise ValueError("Element is not a checkbox or radio button.")

    def uncheck(self, allow_deselected=False) -> "Element":
        """Uncheck this checkbox or radio button.

        Args:
            allow_deselected: Do not raise error if element is already deselected.

        Raises:
            `ValueError` if element is already deselected.
            `ValueError` if element is not a checkbox or radio button

        Returns:
            This element so you can chain another command.
        """
        self.py.log.debug("\t[STEP] .uncheck() - Deselect this checkbox or radio button")
        type_ = self.webelement.get_attribute("type")
        if type_ == "checkbox" or type_ == "radio":
            checked = self.py.webdriver.execute_script("return arguments[0].checked;", self.webelement)
            if checked:
                self.webelement.click()
                return self
            elif allow_deselected:
                return self
            else:
                raise ValueError(f"{type_} is already deselected.")
        raise ValueError("Element is not a checkbox or radio button.")

    def clear(self) -> "Element":
        """Clears the text of the input or textarea element.

            * Only works on elements that can accept text entry.

        Returns:
            This element so you can chain another command.
        """
        self.py.log.debug("\t[STEP] .clear() - Clear the input of this element")
        self.webelement.clear()
        return self

    def click(self, force=False):
        """Clicks the element.

        Args:
            force: If True, a JavascriptExecutor command is sent instead of Selenium's native `.click()`.

        Returns:
            The current instance of Pylenium so you can chain another command.
        """
        self.py.log.debug("\t[STEP] .click() - Click this element")
        if force:
            self.py.webdriver.execute_script("arguments[0].click()", self.webelement)
        else:
            self.webelement.click()
        return self.py

    def deselect(self, value):
        """Deselects all `<option>` within a multi `<select>` element that match the given value.

        Args:
            value: The value or text content of the `<option>` elements to be deselected.

        Raises:
            * `UnexpectedTagNameException` if this element is not a `<select>`
            * `NoSuchElementException` if a matching `<option>` element is not found.

        Returns:
            This dropdown element so you can chain another command.
        """
        self.py.log.debug("\t[STEP] .deselect() - Deselect options from a dropdown element")
        select = Select(self.webelement)
        try:
            select.deselect_by_visible_text(value)
        except NoSuchElementException:
            select.deselect_by_value(value)
        return self

    def double_click(self):
        """Double clicks the element.

        Returns:
            The current instance of Pylenium so you can chain another command.
        """
        self.py.log.debug("\t[STEP] .double_click() - Double click this element")
        ActionChains(self.py.webdriver).double_click(self.webelement).perform()
        return self.py

    def drag_to(self, css: str) -> "Element":
        """Drag the current element to another element given its CSS selector.

        Args:
            css: The CSS selector of the element to drag to.

        Returns:
            The current element.

        Examples:
            py.get('#draggable-card').drag_to('#done-column')
        """
        self.py.log.debug("\t[STEP] .drag_to() - Drag this element to another element")
        to_element = self.py.get(css).webelement
        jquery.drag_and_drop(self.py.webdriver, self.webelement, to_element)
        return self

    def drag_to_element(self, to_element: "Element") -> "Element":
        """Drag the current element to the given element.

        Args:
            to_element: The Element to drag to.

        Returns:
            The current element.

        Examples:
            column = py.get('#done-column')
            py.get('#draggable-card').drag_to_element(column)
        """
        self.py.log.debug("\t[STEP] .drag_to_element() - Drag this element to another element")
        jquery.drag_and_drop(self.py.webdriver, self.webelement, to_element.webelement)
        return self

    def hover(self):
        """Hovers the element.

        Returns:
            The current instance of Pylenium so you can chain another command.
        """
        self.py.log.debug("\t[STEP] .hover() - Hovers this element")
        ActionChains(self.py.webdriver).move_to_element(self.webelement).perform()
        return self.py

    def right_click(self):
        """Right clicks the element.

        Returns:
            The current instance of Pylenium so you can chain another command.
        """
        self.py.log.debug("\t[STEP] .right_click() - Right click this element")
        ActionChains(self.py.webdriver).context_click(self.webelement).perform()
        return self.py

    def select_by_index(self, index: int) -> "Element":
        """Select an `<option>` element within a `<select>` dropdown given its index.

        This is not done by counting the options, but by examining their index attributes.

        Args:
            index: The index position of the `<option>` to be selected.

        Raises:
            * `UnexpectedTagNameException` if the dropdown is not a `<select>` element.
            * `NoSuchElementException` if the `<option>` with the given index doesn't exist.

        Returns:
            The dropdown element so you can chain another command if needed.
        """
        self.py.log.debug("\t[STEP] .select_by_index() - Select an <option> element in this dropdown")
        dropdown = Select(self.webelement)
        dropdown.select_by_index(index)
        return self

    def select_by_text(self, text: str) -> "Element":
        """Selects all `<option>` elements within a `<select>` dropdown given the option's text.

        Args:
            text: The text within the `<option>` to be selected.

        Raises:
            * `UnexpectedTagNameException` if the dropdown is not a `<select>` element.
            * `NoSuchElementException` if the `<option>` with the given text doesn't exist.

        Returns:
            The dropdown element so you can chain another command if needed.
        """
        self.py.log.debug("\t[STEP] .select_by_text() - Select all <option> elements in this dropdown")
        dropdown = Select(self.webelement)
        dropdown.select_by_visible_text(text)
        return self

    def select_by_value(self, value) -> "Element":
        """Selects all `<option>` elements within a `<select>` dropdown given the option's value.

        Args:
            value: The value within the `<option>` to be selected.

        Raises:
            * `UnexpectedTagNameException` if the dropdown is not a `<select>` element.
            * `NoSuchElementException` if the `<option>` with the given value doesn't exist.

        Returns:
            The dropdown element so you can chain another command if needed.
        """
        self.py.log.debug("\t[STEP] .select_by_value() - Select all <option> elements in this dropdown")
        dropdown = Select(self.webelement)
        dropdown.select_by_value(value)
        return self

    def submit(self):
        """Submits the form.

            * Meant for <form> elements. May not have an effect on other types.

        Returns:
            The current instance of Pylenium so you can chain another command.
        """
        self.py.log.debug("\t[STEP] .submit() - Submit the form")
        self.webelement.submit()
        return self.py

    def type(self, *args) -> "Element":
        """Simulate a user typing keys into the input.

        Returns:
            This element so you can chain another command.
        """
        self.py.log.debug("\t[STEP] .type() - Type keys into this element")
        self.webelement.send_keys(args)
        return self

    # FIND ELEMENTS #
    #################

    def contains(self, text: str, timeout: int = None) -> "Element":
        """Gets the DOM element containing the `text`.

        Args:
            text: The text for the element to contain
            timeout: The number of seconds to find the element. Overrides default wait_time.

        Returns:
            The first element that is found, even if multiple elements match the query.
        """
        self.py.log.debug(f"\t[STEP] .contains() - Find the element that contains text: ``{text}``")
        locator = (By.XPATH, f'.//*[contains(text(), "{text}")]')

        if timeout == 0:
            element = self.webelement.find_element(*locator)
        else:
            element = self.py.wait(timeout).until(
                lambda _: self.webelement.find_element(*locator), f"Could not find element with the text ``{text}``"
            )
        return Element(self.py, element, locator)

    def get(self, css: str, timeout: int = None) -> "Element":
        """Gets the DOM element that matches the `css` selector in this element's context.

        Args:
            css: The selector
            timeout: The number of seconds to find the element. Overrides default wait_time.

        Returns:
            The first element that is found, even if multiple elements match the query.
        """
        self.py.log.debug(f"\t[STEP] .get() - Find the element that has css: ``{css}``")
        by = By.CSS_SELECTOR

        if timeout == 0:
            element = self.webelement.find_element(by, css)
        else:
            element = self.py.wait(timeout).until(
                lambda _: self.webelement.find_element(by, css), f"Could not find element with the CSS ``{css}``"
            )
        return Element(self.py, element, locator=(by, css))

    def find(self, css: str, timeout: int = None) -> Elements:
        """Finds all DOM elements that match the `css` selector in this element's context.

        Args:
            css: The selector
            timeout: The number of seconds to find at least one element. Overrides default wait_time.

        Returns:
            A list of the found elements.
        """
        self.py.log.debug(f"\t[STEP] .find() - Find elements with css: ``{css}``")
        by = By.CSS_SELECTOR

        try:
            if timeout == 0:
                elements = self.webelement.find_elements(by, css)
            else:
                elements = self.py.wait(timeout).until(
                    lambda _: self.webelement.find_elements(by, css), f"Could not find any elements with CSS ``{css}``"
                )
        except TimeoutException:
            elements = []
        return Elements(self.py, elements, locator=(by, css))

    def getx(self, xpath: str, timeout: int = None) -> "Element":
        """Finds the DOM element that matches the `xpath` selector.

        Args:
            xpath: The selector to use.
            timeout: The number of seconds to find the element. Overrides default wait_time.

        Returns:
            The first element found, even if multiple elements match the query.
        """
        self.py.log.debug(f"\t[STEP] .getx() - Find the element with xpath: ``{xpath}``")
        by = By.XPATH

        if timeout == 0:
            elements = self.webelement.find_element(by, xpath)
        else:
            elements = self.py.wait(timeout).until(
                lambda _: self.webelement.find_element(by, xpath),
                f"Could not find any elements with the xpath ``{xpath}``",
            )
        return Element(self.py, elements, locator=(by, xpath))

    def findx(self, xpath: str, timeout: int = None) -> "Elements":
        """Finds the DOM elements that matches the `xpath` selector.

        Args:
            xpath: The selector to use.
            timeout: The number of seconds to find at least one element. Overrides default wait_time.

        Returns:
            A list of the found elements.
        """
        self.py.log.debug(f"\t[STEP] .findx() - Find the elements with xpath: ``{xpath}``")
        by = By.XPATH

        try:
            if timeout == 0:
                elements = self.webelement.find_elements(by, xpath)
            else:
                elements = self.py.wait(timeout).until(
                    lambda _: self.webelement.find_elements(by, xpath),
                    f"Could not find any elements with the xpath ``{xpath}``",
                )
        except TimeoutException:
            elements = []
        return Elements(self.py, elements, locator=(by, xpath))

    def children(self) -> Elements:
        """Gets the Child elements."""
        self.py.log.debug("\t[STEP] .children() - Get the children of this element")
        elements = self.py.webdriver.execute_script("return arguments[0].children;", self.webelement)
        return Elements(self.py, elements, None)

    def parent(self) -> "Element":
        """Gets the Parent element."""
        self.py.log.debug("\t[STEP] .parent() - Get the parent of this element")
        js = """
        elem = arguments[0];
        return elem.parentNode;
        """
        element = self.py.webdriver.execute_script(js, self.webelement)
        return Element(self.py, element, None)

    def siblings(self) -> Elements:
        """Gets the Sibling elements."""
        self.py.log.debug("\t[STEP] .siblings() - Get the siblings of this element")
        js = """
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
        """
        elements = self.py.webdriver.execute_script(js, self.webelement)
        return Elements(self.py, elements, None)

    # UTILITIES #
    #############

    def screenshot(self, filename) -> "Element":
        """Take a screenshot of the current element.

        Args:
            filename: the filepath including the filename and extension (like `.png`)

        Examples:
            py.get('#save-button').screenshot('elements/save-button.png')
        """
        self.py.log.debug(f"\t[STEP] .screenshot() - Take a screenshot and save to: ``{filename}``")
        self.webelement.screenshot(filename)
        return self

    def scroll_into_view(self) -> "Element":
        """Scroll this element into view."""
        self.py.log.debug("\t[STEP] .scroll_into_view() - Scroll this element into view")
        self.py.webdriver.execute_script("arguments[0].scrollIntoView(true);", self.webelement)
        return self

    def open_shadow_dom(self) -> "Element":
        """Open a Shadow DOM and return the Shadow Root element.

        Examples:
            shadow1 = py.get('extensions-manager').open_shadow_dom()
            shadow2 = py.get('extensions-list').open_shadow_dom()

        References:
            https://www.seleniumeasy.com/selenium-tutorials/accessing-shadow-dom-elements-with-webdriver
        """
        self.py.log.debug("\t[STEP] .open_shadow_dom() - Open a Shadow DOM and return the Root element")
        shadow_element = self.py.execute_script("return arguments[0].shadowRoot", self.webelement)
        return Element(self.py, shadow_element, locator=None)

    def highlight(self, effect_time=1, color="red", border=5) -> "Element":
        """Highlights (blinks) a Selenium Webdriver element"""

        def apply_style(s):
            self.py.execute_script("arguments[0].setAttribute('style', arguments[1]);", self.webelement, s)

        original_style = self.webelement.get_attribute("style")
        apply_style("border: {0}px solid {1};".format(border, color))
        time.sleep(effect_time)
        apply_style(original_style)

        return self
