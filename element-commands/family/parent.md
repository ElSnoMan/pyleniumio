---
description: The command to get the parent of the current element.
---

# parent

## Syntax

```python
Element.parent() -> Element
```

## Usage

{% code title="correct usage" %}
```python
py.get("li").parent()

---or--- # store in a variable

element = py.get("li").parent()

---or--- # chain an Element command

py.get("li").parent().click()

---or--- # even go up the DOM tree

grand_parent = py.get("li").parent().parent()
```
{% endcode %}

## Arguments

* None

## Yields

* <mark style="color:orange;">**Element**</mark> - The parent Element
