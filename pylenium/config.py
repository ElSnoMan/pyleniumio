from pathlib import Path
from typing import List, Dict

from pydantic import BaseModel

# PYLENIUM CONFIG #
###################


class DriverConfig(BaseModel):
    browser: str = "chrome"
    remote_url: str = ""
    wait_time: int = 10
    page_load_wait_time: int = 0
    options: List[str] = []
    capabilities: Dict = {}
    experimental_options: List[Dict] = None
    seleniumwire_options: Dict = {}
    extension_paths: List[str] = None
    webdriver_kwargs: Dict = None
    version: str = "latest"
    local_path: str = ""


class LoggingConfig(BaseModel):
    pylog_level: str = "debug"
    screenshots_on: bool = True


class ViewportConfig(BaseModel):
    maximize: bool = True
    width: int = 1440
    height: int = 900
    orientation: str = "portrait"


class PyleniumConfig(BaseModel):
    driver: DriverConfig = DriverConfig()
    logging: LoggingConfig = LoggingConfig()
    viewport: ViewportConfig = ViewportConfig()
    custom: dict = {}


# MODELS #
##########


class TestCase(BaseModel):
    name: str
    file_path: Path

    class Config:
        arbitrary_types_allowed = True
