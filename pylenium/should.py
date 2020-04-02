from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec

from pylenium.wait import ElementWait


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

    def disappear(self) -> 'Pylenium':
        """ An expectation that the element is no longer displayed or in the DOM.

        Returns:
            The current element.

        Raises:
            `AssertionError` if the condition is not met in the specified amount of time.
        """
        self._py.log.step('.should().disappear()', True)
        try:
            value = self._wait.until(ec.invisibility_of_element(self._element.webelement))
        except TimeoutException:
            value = False
        if value:
            return self._py
        else:
            self._py.log.failed('.should().disappear()')
            raise AssertionError('Element was still visible or still in the DOM')

    def have_attr(self, attr: str, value: str) -> 'Element':
        """ An expectation that the element has the given attribute with the given value.

        Arguments:
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

    # NEGATIVE CONDITIONS #
    #######################

    def not_be_visible(self) -> 'Element':
        """ An expectation that the element is not displayed but still in the DOM.

        Returns:
            The current element.

        Raises:
            `AssertionError` if the condition is not met in the specified amount of time.
        """
        self._py.log.step('.should().not_be_visible()', True)
        try:
            value = self._wait.until(lambda e: e and not e.is_displayed())
        except TimeoutException:
            value = False

        if value:
            return self._element
        else:
            self._py.log.failed('.should().not_be_visible()')
            raise AssertionError('Element was still visible')

    def not_have_attr(self, attr: str, value: str) -> 'Element':
        """ An expectation that the element does not have the given attribute with the given value.

        Either the attribute does not exist on the element or the value does not match the given value.

        Arguments:
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
