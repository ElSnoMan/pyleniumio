---
description: The command to select an <option> within a <select> element.
---

# select

## Syntax

```python
Element.select(value)
```

## Usage

{% code title="correct usage" %}
```python
py.get('select').select('option-2')

---or--- # chain an Element command

py.get('#dropdown').select('option-1').select('option-2')
```
{% endcode %}

{% code title="incorrect usage" %}
```python
# Errors, can only perform 'select' on a <select> element
py.get('ul > li').select('option-2')
```
{% endcode %}

## Arguments

* `value (str)` - The **text** or **value** or **index** of the option to select.

## Yields

* **\(Element\)** The current instance of Element so you can chain commands.

## Examples

{% code title="select by index" %}
```python
# select the second option in the list
py.get('select').select(1)
```
{% endcode %}

{% code title="select by value or visible text" %}
```python
# select the option with the text or value
py.get('select').select('option2')
```
{% endcode %}

