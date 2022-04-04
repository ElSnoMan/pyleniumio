---
description: The command to get the specified property's value of the element.
---

# get\_property

## Syntax

```python
Element.get_property(property)
```

## Usage

{% code title="correct usage" %}
```python
py.get('.nav-link').get_property('innerHTML')
```
{% endcode %}

{% code title="incorrect usage" %}
```python
# Errors, 'py' cannot call this directly
py.get_property('className')
```
{% endcode %}

## Arguments

* `property (str)`:  The name of the property.

## Yields

* The value returned by the property, but this is usually a string.
