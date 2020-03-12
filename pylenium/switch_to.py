class SwitchTo:
    def __init__(self, pylenium):
        self._py = pylenium

    def frame(self, name_or_id: str):
        """ Switch the driver's context to the new frame.

        Args:
            name_or_id: The frame's `id` or `name` attribute value

        Examples:
            # Switch to an iframe
            py.switch_to_frame('main-frame')
        """
        self._py.wait.until(lambda _: self._py.webdriver.switch_to.frame(name_or_id))
        return self._py

    def parent_frame(self):
        """ Switch the driver's context to the parent frame.

        If the parent frame is the current context, nothing happens.
        """
        self._py.webdriver.switch_to.parent_frame()
        return self._py

    def default_content(self):
        """ Switch the driver's context to the default content. """
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
            self._py.webdriver.switch_to.window(handle)
            return self._py
        elif name_or_handle:
            self._py.webdriver.switch_to.window(name_or_handle)
            return self._py
        else:
            # context unchanged
            return self._py
