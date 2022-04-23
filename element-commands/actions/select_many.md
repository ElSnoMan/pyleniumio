---
description: The command to select multiple <option>s in a multi <select> element.
---

# select\_many

## Syntax

```python
Element.select_many(values)
```

## Usage

{% code title="correct usage" %}
```python
py.get('select').select_many(['option-1', 2])

---or--- # chain a Pylenium command

py.get('select').select_many(['opt-1', 'opt-2']).screenshot('new_view.png')
```
{% endcode %}

{% code title="incorrect usage" %}
```python
# Errors, can only perform 'select_many' on a multi <select> element
py.get('ul > li').select_many(['option-1', 2])
```
{% endcode %}

## Arguments

* `values (list)` - The list of texts or values of the \<option>s you want to select.

## Yields

* **(Pylenium)** The current instance of Pylenium so you can chain commands.
