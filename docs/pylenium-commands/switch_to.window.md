---
description: >-
  The command to switch the driver's context to the specified Window or Browser
  Tab.
---

# switch\_to.window

## Syntax

```python
py.switch_to.window(name_or_handle)
py.switch_to.window(index)
```

## Usage

{% code title="correct usage" %}
```python
# switch to a Window by handle
windows = py.window_handles
py.switch_to.window(name_or_handle=windows[1])
```
{% endcode %}

{% code title="correct usage" %}
```python
# switch to a newly opened Browser Tab by index
py.switch_to.window(index=1)
```
{% endcode %}

## Arguments

* `name_or_handle='' (str)`- The **name** or **window handle** of the Window to switch to
* `index=0 (int)` - The index position of the Window Handle

{% hint style="info" %}
**index=0** will switch to the default content
{% endhint %}

## Yields

* **\(Pylenium\)** The current instance of Pylenium so you can chain commands

