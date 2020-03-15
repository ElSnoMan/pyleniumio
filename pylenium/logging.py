from datetime import datetime


class Logger:
    def __init__(self, test_name, file_path):
        self.test_name = test_name
        self.filepath = f'{file_path}/test_log.txt'
        self._start_log()

    def _start_log(self):
        """ Starts the Test Log. """
        with open(self.filepath, 'w') as file:
            file.write(f'Starting log for {self.test_name}')
            file.write(f'\ntimestamp (UTC): {datetime.utcnow().ctime()}')

    def write(self, string):
        """ Log an entry without a timestamp.

        Args:
            string: The message to log
        """
        with open(self.filepath, 'a') as file:
            file.write(f'\n{string}')

    def write_with_timestamp(self, string):
        """ Log an entry with a UTC timestamp.

        Args:
            string: The message to log
        """
        with open(self.filepath, 'a') as file:
            file.write(f'\n{datetime.utcnow().isoformat()} | {string}')

    def info(self, string, is_subinfo=False):
        """ Logs an INFO entry.

        Args:
            string: The message to log
            is_subinfo: Should the entry be indented?
        """
        if is_subinfo:
            message = f'    [INFO]: {string}'
        else:
            message = f'[INFO]: {string}'
        self.write_with_timestamp(message)

    def step(self, string, is_substep=False):
        """ Logs a STEP entry.

        Args:
            string: The message to log
            is_substep: Should the entry be indented?
        """
        if is_substep:
            message = f'    [STEP]: {string}'
        else:
            message = f'[STEP]: {string}'
        self.write_with_timestamp(message)

    def action(self, string, is_subaction=False):
        """ Logs an ACTION entry.

        Args:
            string: The message to log
            is_subaction: Should the entry be indented?
        """
        if is_subaction:
            message = f'    [ACTION]: {string}'
        else:
            message = f'[ACTION]: {string}'
        self.write_with_timestamp(message)

    def debug(self, string):
        """ Logs a DEBUG entry. """
        self.write_with_timestamp(f'~~~ DEBUG ~~~ :: {string}')

    def warning(self, string):
        """ Logs a WARNING entry. """
        self.write_with_timestamp(f':: warning :: {string}')

    def error(self, string):
        """ Logs an ERROR entry. """
        self.write_with_timestamp(f':: error :: {string}')

    def passed(self, string):
        """ Logs a PASSED entry. """
        self.write_with_timestamp(f'** [PASSED] ** {string}')

    def failed(self, string):
        """ Logs a FAILED entry. """
        self.write_with_timestamp(f'!! [FAILED] !! {string}')