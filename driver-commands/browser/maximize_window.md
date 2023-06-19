---
description: The command the maximize the current window.
---

# maximize\_window

## Syntax

```python
py.maximize_window() -> Pylenium
```

## Usage

{% code title="correct usage" %}
```python
# By default, Pylenium will maximize the window for you, but just in case...
py.maximize_window().visit("https://qap.dev")
```
{% endcode %}

## Arguments

* None

## Yields

* <mark style="color:orange;">**Pylenium**</mark> - The current instance of Pylenium so you can chain commands
