---
description: The command to get the attribute's value with the given name.
---

# get\_attribute

## Syntax

```python
Element.get_attribute(attribute: str) -> bool | str | None
```

## Usage

{% code title="correct usage" %}
```python
py.get("a").get_attribute("href")

---or--- # store in a variable

href = py.get("a").get_attribute("href")
assert href.startswith("https://")
```
{% endcode %}

## Arguments

* <mark style="color:purple;">`attribute (str)`</mark> = The name of the attribute to find in the Element

## Yields

* If the value is <mark style="color:purple;">`"true"`</mark> or <mark style="color:purple;">`"false"`</mark>, then this returns a bool of <mark style="color:yellow;">**True**</mark> or <mark style="color:yellow;">**False**</mark>
* If the name does not exist, return <mark style="color:yellow;">**None**</mark>
* All other values are returned as <mark style="color:yellow;">**strings**</mark>
