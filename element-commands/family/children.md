---
description: The command to get the children of the current element.
---

# children

## Syntax

```python
Element.children() -> Elements
```

## Usage

{% code title="correct usage" %}
```python
py.get("a").children()

---or--- # store in a variable

elements = py.get("ul").children()

---or--- # chain another command

child = py.get("ul").children().first()
```
{% endcode %}

## Arguments

* None

## Yields

* <mark style="color:orange;">**Elements**</mark> - A list of Elements. The list is empty if no children are found.
