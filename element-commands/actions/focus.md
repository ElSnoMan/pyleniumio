---
description: The command to switch focus to the element.
---

# focus

## Syntax

```python
Element.focus() -> Element
```

## Usage

{% code title="correct usage" %}
```python
py.get(".menu").focus()
```
{% endcode %}

{% code title="incorrect usage" %}
```python
# Errors, Pylenium doesn't have a focus() command
py.focus()
```
{% endcode %}

## Arguments

* None

## Yields

* <mark style="color:orange;">**Element**</mark> - The element that has been focused
