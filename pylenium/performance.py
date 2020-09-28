from typing import Union, List

from pydantic import BaseModel, Field


class Performance:
    def __init__(self, webdriver):
        self._webdriver = webdriver

    def get_navigation_timing(self):
        js = 'return window.performance.getEntriesByType("navigation")[0];'
        return NavigationTiming(**self._webdriver.execute_script(js))


class NavigationTiming(BaseModel):
    connect_end: float = Field(alias='connectEnd')
    connect_start: float = Field(alias='connectStart')
    decoded_body_size: Union[int, float] = Field(alias='decodedBodySize')
    dom_complete: float = Field(alias='domComplete')
    dom_content_loaded_event_end: float = Field(alias='domContentLoadedEventEnd')
    dom_content_loaded_event_start: float = Field(alias='domContentLoadedEventStart')
    time_to_interactive: float = Field(alias='domInteractive')
    domain_lookup_end: float = Field(alias='domainLookupEnd')
    domain_lookup_start: float = Field(alias='domainLookupStart')
    duration: float
    encoded_body_size: Union[int, float] = Field(alias='encodedBodySize')
    entry_type: str = Field(alias='entryType')
    fetch_start: float = Field(alias='fetchStart')
    initiator_type: str = Field(alias='initiatorType')
    load_event_end: float = Field(alias='loadEventEnd')
    load_event_start: float = Field(alias='loadEventStart')
    name: str
    next_hop_protocol: str = Field(alias='nextHopProtocol')
    redirect_count: int = Field(alias='redirectCount')
    redirect_end: int = Field(alias='redirectEnd')
    redirect_start: int = Field(alias='redirectStart')
    request_start: float = Field(alias='requestStart')
    response_end: float = Field(alias='responseEnd')
    response_start: float = Field(alias='responseStart')
    secure_connection_start: float = Field(alias='secureConnectionStart')
    server_timing: List = Field(alias='serverTiming')
    start_time: int = Field(alias='startTime')
    transfer_size: Union[int, float] = Field(alias='transferSize')
    type: str
    unload_event_end: int = Field(alias='unloadEventEnd')
    unload_event_start: int = Field(alias='unloadEventStart')
    worker_start: Union[int, float] = Field(alias='workerStart')
