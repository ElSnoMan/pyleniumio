---
description: >-
  The command to drag the current element to another element given its CSS
  selector.
---

# drag\_to

## Syntax

```python
Element.drag_to(css)
```

## Usage

{% code title="correct usage" %}
```python
py.get('#drag-this').drag_to('#drop-here')

---or---

from_element = py.get('#drag-this')
from_element.drag_to('#drop-here')
```
{% endcode %}

{% code title="incorrect usage" %}
```python
# Errors, 'drag_to' takes a CSS selector string

to_element = py.get('#drop-here')
py.get('#drag-this').drag_to(to_element)

# Use the .drag_to_element() command instead
```
{% endcode %}

## Arguments

* `css(str)` - The CSS selector of the element to drag to.

## Yields

* **(Element)** The current element that was dragged.
