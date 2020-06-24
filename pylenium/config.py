from typing import List

from pydantic import BaseModel

# PYLENIUM CONFIG #
###################


class DriverConfig(BaseModel):
    browser: str = 'chrome'
    remote_url: str = ''
    wait_time: int = 10
    page_load_wait_time: int = 0
    options: List[str] = []
    capabilities: dict = {}
    experimental_options: List[dict] = None
    extension_paths: List[str] = None
    version: str = 'latest'


class LoggingConfig(BaseModel):
    pylog_level: str = 'info'
    screenshots_on: bool = True


class ViewportConfig(BaseModel):
    maximize: bool = True
    width: int = 1440
    height: int = 900
    orientation: str = 'portrait'


class PyleniumConfig(BaseModel):
    driver: DriverConfig = DriverConfig()
    logging: LoggingConfig = LoggingConfig()
    viewport: ViewportConfig = ViewportConfig()
    custom: dict = {}


# MODELS #
##########

class TestCase(BaseModel):
    name: str
    file_path: str

    class Config:
        arbitrary_types_allowed = True
