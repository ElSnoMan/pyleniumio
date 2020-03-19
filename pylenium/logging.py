import os
import time
from datetime import datetime


log_levels = [
    'off',  # turn off all logging
    'info',  # (default) INFO, STEP, ACTION
    'debug'  # info + DEBUG, WARNING, ERROR
]


class Logger:
    def __init__(self, test_name, file_path, pylog_level='info'):
        self.pylog_level = pylog_level
        self.test_name = test_name
        self.filepath = f'{file_path}/test_log.txt'
        self._start_log()

    def _start_log(self):
        """ Starts the Test Log. """
        with open(self.filepath, 'w') as file:
            file.write(f'Starting log for {self.test_name}')
            file.write(f'\ntimestamp (UTC): {datetime.utcnow().ctime()}')
            file.write(f'\npylog_level: {self.pylog_level.upper()}')

    def _wait_for_log(self):
        retries = 0
        while retries < 3:
            if not os.path.exists(self.filepath):
                time.sleep(1)
                retries += 1
            else:
                break

    def write(self, string):
        """ Log an entry without a timestamp.

        Args:
            string: The message to log
        """
        self._wait_for_log()
        with open(self.filepath, 'a') as file:
            file.write(f'\n{string}')

    def write_with_timestamp(self, string):
        """ Log an entry with a UTC timestamp.

        Args:
            string: The message to log
        """
        self._wait_for_log()
        with open(self.filepath, 'a') as file:
            file.write(f'\n{datetime.utcnow().isoformat()} | {string}')

    def info(self, string, is_subinfo=False):
        """ Logs an INFO entry.

        Ignore when log_level is 'off'

        Args:
            string: The message to log
            is_subinfo: Should the entry be indented?
        """
        if self.pylog_level == 'off':
            return

        if is_subinfo:
            message = f'    [INFO]: {string}'
        else:
            message = f'[INFO]: {string}'
        self.write_with_timestamp(message)

    def step(self, string, is_substep=False):
        """ Logs a STEP entry.

        Ignore when log_level is 'off'

        Args:
            string: The message to log
            is_substep: Should the entry be indented?
        """
        if self.pylog_level == 'off':
            return

        if is_substep:
            message = f'    [STEP]: {string}'
        else:
            message = f'[STEP]: {string}'
        self.write_with_timestamp(message)

    def action(self, string, is_subaction=False):
        """ Logs an ACTION entry.

        Ignore when log_level is 'off'

        Args:
            string: The message to log
            is_subaction: Should the entry be indented?
        """
        if self.pylog_level == 'off':
            return

        if is_subaction:
            message = f'    [ACTION]: {string}'
        else:
            message = f'[ACTION]: {string}'
        self.write_with_timestamp(message)

    def debug(self, string):
        """ Logs a DEBUG entry.

        Ignore when log_level is 'off' or 'info'
        """
        if self.pylog_level == 'off' or self.pylog_level == 'info':
            return

        self.write_with_timestamp(f'~~~ DEBUG ~~~ :: {string}')

    def warning(self, string):
        """ Logs a WARNING entry.

        Ignore when log_level is 'off' or 'info'
        """
        if self.pylog_level == 'off' or self.pylog_level == 'info':
            return

        self.write_with_timestamp(f':: warning :: {string}')

    def error(self, string):
        """ Logs an ERROR entry.

        Ignore when log_level is 'off' or 'info'
        """
        if self.pylog_level == 'off' or self.pylog_level == 'info':
            return

        self.write_with_timestamp(f':: error :: {string}')

    def passed(self, string):
        """ Logs a PASSED entry.

        Ignore when log_level is 'off'
        """
        if self.pylog_level == 'off':
            return

        self.write_with_timestamp(f'** [PASSED] ** {string}')

    def failed(self, string):
        """ Logs a FAILED entry.

        Ignore when log_level is 'off'
        """
        if self.pylog_level == 'off':
            return

        self.write_with_timestamp(f'!! [FAILED] !! {string}')
