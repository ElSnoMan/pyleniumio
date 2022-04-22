---
description: The command to scroll to the given location.
---

# scroll\_to

## Syntax

```python
py.scroll_to(x: int, y: int) -> Pylenium
```

## Usage

{% code title="correct usage" %}
```python
# scroll down 500px
py.scroll_to(0, 500)
```
{% endcode %}

## Arguments

* <mark style="color:purple;">**`x (int)`**</mark>: The number of pixels to scroll horizontally
* <mark style="color:purple;">**`y (int)`**</mark>: The number of pixels to scroll vertically

## Yields

* <mark style="color:orange;">**Pylenium**</mark> - so you can chain another command
