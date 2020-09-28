# PaintTiming
# Resources


def test_get_time_to_interactive(py):
    py.visit('https://demoqa.com')
    time_to_interactive = py.performance.get_navigation_timing().time_to_interactive
    assert isinstance(time_to_interactive, float)


def test_get_navigation_timing_object(py):
    py.visit('https://demoqa.com')
    assert py.performance.get_navigation_timing()
