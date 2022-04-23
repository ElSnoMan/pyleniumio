---
description: Get the CSS Value of the element given the property name.
---

# css\_value

## Syntax

```python
Element.css_value(property_name: str) -> Any
```

## Usage

{% code title="correct usage" %}
```python
py.get("a").css_value("background-color")

---or--- # chain a Pylenium command

py.find("a").first().get("span").css_value("color")
```
{% endcode %}

{% code title="incorrect usage" %}
```python
# Errors, 'Pylenium' yields Pylenium, not Element
py.css_value("color")

---or---

# Errors, 1 is not a valid property name
py.get("#button").css_value(1)
```
{% endcode %}

## Arguments

* <mark style="color:purple;">**`property_name (str)`**</mark> - The name of the CSS Property

## Yields

* <mark style="color:orange;">**Any**</mark> - Typically strings, but this depends on the CSS Property
