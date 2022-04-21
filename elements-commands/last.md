---
description: The command to get the last Element in a list of Elements.
---

# last

## Syntax

```python
Elements.last() -> Element
```

## Usage

{% code title="correct usage" %}
```python
py.find("li").last()

---or--- # store in a variable

last = py.xpath("//a").last()

---or--- # chain an Element command

py.get("ul > li").children().last().click()
```
{% endcode %}

{% code title="incorrect usage" %}
```python
# Errors, 'get' yields Element, not Elements
py.get("ul > li").last()
```
{% endcode %}

## Arguments

* None

## Yields

* <mark style="color:orange;">**Element**</mark> - The last Element in a list of Elements

## Raises

* **IndexError** if Elements is empty
