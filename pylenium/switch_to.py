from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchFrameException
from pylenium.element import Element


class FrameIsAvailable:
    """Expected Condition since the current one from Selenium doesn't work for strings, only tuples."""

    def __init__(self, frame_name_or_id):
        self.frame_name_or_id = frame_name_or_id

    def __call__(self, driver):
        try:
            driver.switch_to.frame(self.frame_name_or_id)
            return True
        except NoSuchFrameException:
            return False


class SwitchTo:
    def __init__(self, pylenium):
        self._py = pylenium

    def frame(self, name_or_id: str, timeout: int = 0):
        """Switch the driver's context to a frame given the name or id of the element.

        Args:
            name_or_id: The frame's `id` or `name` attribute value
            timeout: The number of seconds to wait for the frame to be switched to.

        Examples:
            # Switch to an iframe
            py.switch_to.frame('main-frame')
        """
        self._py.log.debug(f"[STEP] py.switch_to.frame() - Switch to frame using name or id: ``{name_or_id}``")
        self._py.wait(timeout).until(FrameIsAvailable(name_or_id))
        return self._py

    def frame_by_element(self, element: Element, timeout: int = 0):
        """Switch the driver's context to the given frame element.

        Args:
            element (Element): The frame element to switch to
            timeout: The number of seconds to wait for the frame to be switched to.

        Examples:
            iframe = py.get('iframe')
            py.switch_to.frame_by_element(iframe)
        """
        self._py.log.debug("[STEP] py.switch_to.frame_by_element() - Switch to frame using an Element.")
        self._py.wait(timeout).until(ec.frame_to_be_available_and_switch_to_it(element.locator))
        return self._py

    def parent_frame(self):
        """Switch the driver's context to the parent frame.

        If the parent frame is the current context, nothing happens.
        """
        self._py.log.debug("[STEP] py.switch_to.parent_frame() - Switch to the parent frame")
        self._py.webdriver.switch_to.parent_frame()
        return self._py

    def default_content(self):
        """Switch the driver's context to the default content."""
        self._py.log.debug("[STEP] py.switch_to.default_content() - Switch to default content of this browser session")
        self._py.webdriver.switch_to.default_content()
        return self._py

    def new_window(self):
        """Open a new Browser Window and switch the driver's context (aka focus) to it."""
        self._py.webdriver.switch_to.new_window("window")
        return self._py

    def new_tab(self):
        """Open a new Browser Tab and switch the driver's context (aka focus) to it."""
        self._py.webdriver.switch_to.new_window("tab")
        return self._py

    def window(self, name_or_handle="", index=0):
        """Switch the driver's context (aka focus) to the specified Browser Window or Browser Tab.

        Args:
            name_or_handle: The name or window handle of the Window or Tab to switch to.
            index: The index position of the Window Handle.

        * `index=0` would be the default content.

        Examples:
            # Switch to a Window by handle
            windows = py.window_handles
            py.switch_to.window(name_or_handle=windows[1])

            # Switch to a newly opened Browser Tab by index
            py.switch_to.window(index=1)
        """
        if index:
            handle = self._py.webdriver.window_handles[index]
            self._py.log.debug(f"[STEP] py.switch_to.window() - Switch to a Tab or Window by index: ``{index}``")
            self._py.webdriver.switch_to.window(handle)
            return self._py
        elif name_or_handle:
            self._py.log.debug(
                f"[STEP] py.switch_to.window() - Switch to Tab or Window by name or handle: ``{name_or_handle}``"
            )
            self._py.webdriver.switch_to.window(name_or_handle)
            return self._py
        else:
            # context unchanged
            return self._py
