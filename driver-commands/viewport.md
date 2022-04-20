---
description: The command to control the size and orientation of the current browser window.
---

# viewport

## Syntax

```python
py.viewport(width, height)
py.viewport(width, height, orientation)
```

## Usage

{% code title="correct usage" %}
```python
py.viewport(1280, 800) # macbook-13 size
```
{% endcode %}

## Arguments

* `width` - The width in pixels
* `height` - The height in pixels
* `orientation='portrait' (str)` - Pass `'landscape'` to reverse the width and height

## Yields

* **(Pylenium)** The current instance of Pylenium so you can change commands

## Examples

```python
py.viewport(1280, 800) # macbook-13 size
py.viewport(1440, 900) # macbook-15 size
py.viewport(375, 667, orientation='landscape')  # iPhone X size
```
