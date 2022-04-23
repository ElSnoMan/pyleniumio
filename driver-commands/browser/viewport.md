---
description: The command to control the size and orientation of the current browser window.
---

# viewport

## Syntax

```python
py.viewport(width: int, height: int) -> Pylenium
py.viewport(width: int, height: int, orientation: str) -> Pylenium
```

## Usage

{% code title="correct usage" %}
```python
py.viewport(1280, 800) # macbook-13 size
```
{% endcode %}

## Arguments

* <mark style="color:purple;">`width (int)`</mark> - The width in pixels
* <mark style="color:purple;">`height (int)`</mark> - The height in pixels
* <mark style="color:purple;">`orientation="portrait" (str)`</mark> - Pass <mark style="color:purple;">`"landscape"`</mark> to reverse the width and height

## Yields

* <mark style="color:orange;">**Pylenium**</mark> - The current instance of Pylenium so you can change commands

## Examples

```python
py.viewport(1280, 800) # macbook-13 size
py.viewport(1440, 900) # macbook-15 size
py.viewport(375, 667, orientation="landscape")  # iPhone X size
```
