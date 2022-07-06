"""Custom Logging for Pylenium

Log Levels:
    CRITICAL = 50,
    ERROR    = 40,
    WARNING  = 30,
    USER     = 25, *
    INFO     = 20,
    COMMAND  = 15, * (default)
    DEBUG    = 10
"""

import logging
from rich.logging import RichHandler


COMMAND_LOG_LEVEL = 15
COMMAND_LOG_LEVEL_NAME = "COMMAND"
USER_LOG_LEVEL = 25
USER_LOG_LEVEL_NAME = "USER"


# Add the levels
logging.addLevelName(COMMAND_LOG_LEVEL, COMMAND_LOG_LEVEL_NAME)
logging.COMMAND = COMMAND_LOG_LEVEL
logging.addLevelName(USER_LOG_LEVEL, USER_LOG_LEVEL_NAME)
logging.USER = USER_LOG_LEVEL_NAME

# Create logger
logger = logging.getLogger("PYL")
logger.setLevel(logging.COMMAND)

# Configure logger
# DATE_FORMAT = "%Y/%m/%d %H:%M:%S"
logger.addHandler(RichHandler(rich_tracebacks=True, markup=True))


def command(self, message: str, *args, **kwargs) -> None:
    """Log a command message.

    Args:
        message: The message to log (the string must be in "%s" format. No f-strings)

    Examples:
        def visit(self, url):
            log.command("py.visit() - Visit URL: %s", url)
            ...
    """
    # Yes, logger takes its '*args' as 'args'.
    if self.isEnabledFor(COMMAND_LOG_LEVEL):
        self._log(COMMAND_LOG_LEVEL, message, args, **kwargs)


def this(self, message: str, *args, **kwargs) -> None:
    """Log a message above the INFO log level.

    * This is a convenient, custom log level for Pylenium users to use if needed

    Args:
        message: the message to log (the string must be in "%s" format. No f-strings)

    Examples:
        def add_to_cart(self, item: str, quantity: int):
            log.this("Add items to cart: item=%s - qty=%s", item, quantity)
            ...
    """
    # Yes, logger takes its '*args' as 'args'.
    if self.isEnabledFor(USER_LOG_LEVEL):
        self._log(USER_LOG_LEVEL, message, args, **kwargs)


# Register the new loging functions
logging.Logger.command = command
logging.Logger.this = this
