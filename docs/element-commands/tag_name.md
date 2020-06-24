---
description: The command that gets the current Element's tag name.
---

# tag\_name

## Syntax

```python
Element.tag_name()
```

## Usage

{% code title="correct usage" %}
```python
assert py.get('.btn').tag_name() == 'button'
```
{% endcode %}

{% code title="incorrect usage" %}
```python
# Errors, 'tag_name' is not a property
py.get('a').tag_name
```
{% endcode %}

## Arguments

* None

## Yields

* **\(str\)** The tag name of the current Element

