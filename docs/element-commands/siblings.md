---
description: The command to get the siblings of the element.
---

# siblings

## Syntax

```python
Element.siblings()
```

## Usage

{% code title="correct usage" %}
```python
py.get('a').siblings()

---or--- # store in a variable

elements = py.get('.nav-link').siblings()

---or--- # chain an Elements command

sibling = py.get('ul').siblings().first()
```
{% endcode %}

## Arguments

* None

## Yields

* **(Elements)** A list of Elements. The list is empty if no siblings are found.
