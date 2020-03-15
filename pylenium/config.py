from pydantic import BaseModel
from pylenium.logging import Logger

# PYLENIUM CONFIG #
###################


class DriverConfig(BaseModel):
    browser: str
    remote_url: str
    wait_time: int = 10


class ViewportConfig(BaseModel):
    maximize: bool = True
    width: int
    height: int
    orientation: str


class PyleniumConfig(BaseModel):
    driver: DriverConfig
    viewport: ViewportConfig


# MODELS #
##########

class TestCase(BaseModel):
    name: str
    file_path: str
    logger: Logger

    class Config:
        arbitrary_types_allowed = True
