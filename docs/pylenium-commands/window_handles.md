---
description: >-
  This property gets a list of all the window handles in the current browser
  session.
---

# window\_handles

## Syntax

```python
py.window_handles
```

## Usage

{% code title="correct usage" %}
```python
# this property is mainly used to switch to windows or tabs

# assert that there are two windows - the main website and a new tab
windows = py.window_handles
assert len(windows) == 2

# then switch to the new tab
py.switch_to.window(name_or_handle=windows[1])
```
{% endcode %}

## Arguments

* None

## Yields

* **List\[str]** A list of all the window handles in the current browser session.
