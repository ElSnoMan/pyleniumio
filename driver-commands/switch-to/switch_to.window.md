---
description: >-
  The command to switch the driver's context to the specified Window or Browser
  Tab.
---

# window

## Syntax

```python
py.switch_to.window(name_or_handle: str) -> Pylenium
py.switch_to.window(index: int) -> Pylenium
```

## Usage

{% code title="correct usage" %}
```python
# Switch to a Window by handle
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

* <mark style="color:purple;">`name_or_handle="" (str)`</mark> - The **name** or **window handle** of the Window to switch to
* <mark style="color:purple;">`index=0 (int)`</mark> - The index position of the Window Handle

{% hint style="info" %}
**index=0** will switch to the default content
{% endhint %}

## Yields

* <mark style="color:orange;">**Pylenium**</mark> - The current instance of Pylenium so you can chain commands
