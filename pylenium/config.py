from typing import List

from pydantic import BaseModel
from pylenium.logging import Logger

# PYLENIUM CONFIG #
###################


class DriverConfig(BaseModel):
    browser: str = 'chrome'
    remote_url: str = ''
    wait_time: int = 10
    options: List[str]


class LoggingConfig(BaseModel):
    pylog_level: str = 'info'
    screenshots_on: bool = True


class ViewportConfig(BaseModel):
    maximize: bool = True
    width: int = 1440
    height: int = 900
    orientation: str = 'portrait'


class PyleniumConfig(BaseModel):
    driver: DriverConfig
    logging: LoggingConfig
    viewport: ViewportConfig


# MODELS #
##########

class TestCase(BaseModel):
    name: str
    file_path: str
    logger: Logger

    class Config:
        arbitrary_types_allowed = True
