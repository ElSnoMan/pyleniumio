---
description: The command to drag the current element to the given element.
---

# drag\_to\_element

## Syntax

```python
Element.drag_to_element(to_element)
```

## Usage

{% code title="correct usage" %}
```python
element = py.get('#drop-here')
py.get('#drag-this').drag_to_element(element)
```
{% endcode %}

{% code title="incorrect usage" %}
```python
# Errors, 'drag_to_element' takes an Element
py.get('#drag-this').drag_to_element('#drop-here')

# Use the .drag_to() command instead

---or---

# Errors, `drag_to_element` and `drag_to` are not part of the Pylenium object
element = py.get('#drop-here')
py.drag_to_element(element)
```
{% endcode %}

## Arguments

* `to_element(Element)` - The destination element to drag to.

## Yields

* **(Element)** The current element that was dragged.
