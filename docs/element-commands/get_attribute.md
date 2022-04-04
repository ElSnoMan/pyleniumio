---
description: The command to get the attribute's value with the given name.
---

# get\_attribute

## Syntax

```python
Element.get_attribute(attribute)
```

## Usage

{% code title="correct usage" %}
```python
py.get('a').get_attribute('href')

---or--- # store in a variable

href = py.get('a').get_attribute('href')
```
{% endcode %}

## Arguments

* `attribute (str)` = The name of the attribute to find in the Element

## Yields

* If the value is `'true'` or `'false"`, then this returns a bool of **True** or **False**
* If the name does not exist, return **None**
* All other values are returned as strings
