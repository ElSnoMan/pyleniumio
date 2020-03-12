from pydantic import BaseModel


class DriverConfig(BaseModel):
    wait_time: int = 10


class ViewportConfig(BaseModel):
    maximize: bool = True
    width: int
    height: int
    orientation: str


class PyleniumConfig(BaseModel):
    driver: DriverConfig
    viewport: ViewportConfig
