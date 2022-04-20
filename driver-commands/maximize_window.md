---
description: The command the maximize the current window.
---

# maximize\_window

## Syntax

```python
py.maximize_window()
```

## Usage

{% code title="correct usage" %}
```python
# by default, Pylenium will maximaze the window for you, but just in case...
py.maximize_window().visit('https://qap.dev')
```
{% endcode %}

## Arguments

* None

## Yields

* **(Pylenium)** The current instance of Pylenium so you can chain commands
