import pytest

from pylenium.driver import Pylenium


@pytest.fixture
def qap_dev(py) -> Pylenium:
    py.visit('https://qap.dev')
    py.getx('//*[contains(@class, "Footer") and text()="Present at QAP"]').should().be_visible()
    return py


def test_custom_perf_metrics(qap_dev):
    """ Check Pylenium's native web performance metrics.

    These data points are not part of W3C's Performance APIs and are our own calculations.
    """
    perf = qap_dev.performance.get()
    assert perf.page_load_time()
    assert perf.time_to_first_byte()
    assert perf.time_to_first_contentful_paint()
    assert perf.time_to_interactive()
    assert perf.number_of_requests()
    assert perf.time_to_dom_content_loaded()
    assert perf.page_weight()
    assert perf.connection_time()
    assert perf.request_time()
    assert perf.fetch_time()


def test_get_timing_objects(qap_dev):
    """ Check retrievals and schemas. """
    assert qap_dev.performance.get_navigation_timing()
    assert qap_dev.performance.get_paint_timing()
    assert qap_dev.performance.get_resources()
    assert qap_dev.performance.get_time_origin()
