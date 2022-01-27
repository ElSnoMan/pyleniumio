""" Chrome DevTools Protocol - Performance Tab """
from pylenium.driver import Pylenium


def test_capture_performance_metrics(py: Pylenium):
    py.visit("https://qap.dev")
    metrics = py.cdp.get_performance_metrics()
    assert metrics["metrics"]
    assert metrics["metrics"][0]["name"] == "Timestamp"
    assert metrics["metrics"][0]["value"] > 0
