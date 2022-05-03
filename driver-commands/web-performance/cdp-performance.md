---
description: Chrome DevTools Protocol Performance API to capture metrics.
---

# CDP Performance

**Selenium 4** uses the <mark style="color:yellow;">**Chrome DevTools Protocol**</mark> which has a <mark style="color:orange;">`"Performance.getMetrics"`</mark> command! Pylenium provides a simple wrapper to capture these metrics.

## Syntax

```python
py.cdp.get_performance_metrics() -> Dict
```

## Usage

The <mark style="color:yellow;">**Dictionary**</mark> of performance metrics returned includes metrics like:

* ScriptDuration
* ThreadTime
* ProcessTime
* DomContentLoaded

{% code title="correct usage" %}
```python
metrics = py.cdp.get_performance_metrics()
```
{% endcode %}

{% code title="dictionary" %}
```python
{'metrics':
  [
    {'name': 'Timestamp', 'value': 425608.80694},
    {'name': 'AudioHandlers', 'value': 0},
    {'name': 'ThreadTime', 'value': 0.002074},
    ...
  ]
}
```
{% endcode %}

## Arguments

* None

## Yields

* <mark style="color:yellow;">**Dict**</mark>

## Examples

```python
def test_capture_performance_metrics(py: Pylenium):
    py.visit("https://qap.dev")
    metrics = py.cdp.get_performance_metrics()["metrics"]
    assert metrics
    assert metrics[0]["name"] == "Timestamp"
    assert metrics[0]["value"] > 0
```
