---
description: The command to get the first Element in a list of Elements.
---

# first

## Syntax

```python
Elements.first() -> Element
```

## Usage

{% code title="correct usage" %}
```python
py.find("li").first()

---or--- # store in a variable

element = py.xpath("//a").first()

---or--- # chain an Element command

py.get("ul > li").children().first().click()
```
{% endcode %}

{% code title="incorrect usage" %}
```python
# Errors, 'get' yields Element, not Elements
py.get("ul > li").first()
```
{% endcode %}

## Arguments

* None

## Yields

* <mark style="color:orange;">**Element**</mark> - The first Element in the list of Elements

## Raises

* **IndexError** if Elements is empty
