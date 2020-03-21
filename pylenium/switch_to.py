from selenium.common.exceptions import NoSuchFrameException
from selenium.webdriver.support import expected_conditions as ec


class SwitchTo:
    def __init__(self, pylenium):
        self._py = pylenium

    def frame(self, name_or_id: str, timeout: int = 0):
        """ Switch the driver's context to the new frame.

        Args:
            name_or_id: The frame's `id` or `name` attribute value
            timeout: The number of seconds to wait for the frame to be switched to.

        Examples:
            # Switch to an iframe
            py.switch_to.frame('main-frame')
        """
        self._py.log.action(f'py.switch_to.frame() - Switch to frame using name or id: ``{name_or_id}``')
        self._py.wait(timeout).until(ec.frame_to_be_available_and_switch_to_it(name_or_id))
        return self._py

    def parent_frame(self):
        """ Switch the driver's context to the parent frame.

        If the parent frame is the current context, nothing happens.
        """
        self._py.log.action('py.switch_to.parent_frame() - Switch to the parent frame')
        self._py.webdriver.switch_to.parent_frame()
        return self._py

    def default_content(self):
        """ Switch the driver's context to the default content. """
        self._py.log.action('py.switch_to.default_content() - Switch to the default content of this browser session')
        self._py.webdriver.switch_to.default_content()
        return self._py

    def window(self, name_or_handle='', index=0):
        """ Switch the driver's context to the specified Window or Browser Tab.

        Args:
            name_or_handle: The name or window handle of the Window to switch to.
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
            self._py.log.action(f'py.switch_to.window() - Switch to a Tab or Window by index: ``{index}``')
            self._py.webdriver.switch_to.window(handle)
            return self._py
        elif name_or_handle:
            self._py.log.action(f'py.switch_to.window() - Switch to a Tab or Window by name or handle: ``{name_or_handle}``')
            self._py.webdriver.switch_to.window(name_or_handle)
            return self._py
        else:
            # context unchanged
            return self._py
