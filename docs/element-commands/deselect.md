---
description: The command to deselect an <option> within a multi <select> element.
---

# deselect

## Syntax

```python
Element.deselect(value)
```

## Usage

{% code title="correct usage" %}
```python
py.get('select').deselect('option-2')

---or--- # chain a Pylenium command

py.get('select').deselect('locked').get('#start-edit').click()
```
{% endcode %}

{% code title="incorrect usage" %}
```python
# Errors, can only perform 'deselect' on <select> elements
py.get('ul > li').deselect('option-2')
```
{% endcode %}

## Arguments

* `value (str)` - The text or value of the option to deselect.

## Yields

* **(Pylenium)** The current instance of Pylenium so you can chain commands.
