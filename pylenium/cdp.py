""" Chrome DevTools Protocol (CDP) introduced in Selenium 4.

Resources:
    - https://www.selenium.dev/documentation/webdriver/bidirectional/chrome_devtools/
    - https://chromedevtools.github.io/devtools-protocol/

* Currently only supports the Chrome Browser, although some chromium browsers may work as well.
"""

from typing import Dict


class CDP:
    """Chrome DevTools Protocol."""

    def __init__(self, webdriver):
        self._webdriver = webdriver

    def execute_command(self, cmd: str, cmd_args: Dict) -> Dict:
        """Execute Chrome Devtools Protocol command and get returned result.

        The command and command args should follow chrome devtools protocol domains/commands, refer to link
        https://chromedevtools.github.io/devtools-protocol/

        Args:
            cmd: The command name
            cmd_args: The command args. Pass an empty dict {} if there is no command args

        Examples:
            py.cdp.execute_command('Network.getResponseBody', {'requestId': requestId})

        Returns:
            A dict of results or an empty dict {} if there is no result to return.
            For example, to getResponseBody:
            {'base64Encoded': False, 'body': 'response body string'}
        """
        return self._webdriver.execute_cdp_cmd(cmd, cmd_args)

    def get_performance_metrics(self) -> Dict:
        """Get performance metrics from Chrome DevTools - similar to the Performance tab in Chrome.

        Examples:
            metrics = py.cdp.get_performance_metrics()

        Returns:
            A dict of performance metrics including 'ScriptDuration', 'ThreadTime', 'ProcessTime', and 'DomContentLoaded'.

            {'metrics': [
                {'name': 'Timestamp', 'value': 425608.80694},
                {'name': 'AudioHandlers', 'value': 0},
                {'name': 'ThreadTime', 'value': 0.002074},
                ...
                ]
            }
        """
        # The commented out code below should have been executed prior to this function call.
        # self._webdriver.execute_cdp_cmd("Performance.enable", {})
        return self._webdriver.execute_cdp_cmd("Performance.getMetrics", {})
