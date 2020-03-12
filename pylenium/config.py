from pydantic import BaseModel


class DriverConfig(BaseModel):
    wait_time: int


class ViewportConfig(BaseModel):
    width: int
    height: int
    orientation: str


class PyleniumConfig(BaseModel):
    driver: DriverConfig
    viewport: ViewportConfig
