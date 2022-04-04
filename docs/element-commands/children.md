---
description: The command to get the children of the element.
---

# children

## Syntax

```python
Element.children()
```

## Usage

{% code title="correct usage" %}
```python
py.get('a').children()

---or--- # store in a variable

elements = py.get('ul').children()

---or--- # chain another command

child = py.get('ul').children().first()
```
{% endcode %}

## Arguments

* None

## Yields

* **(Elements)** A list of Elements. The list is empty if no children are found.
