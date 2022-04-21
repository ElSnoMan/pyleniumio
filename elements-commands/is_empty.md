---
description: The command to check if the list of elements is empty.
---

# is\_empty

## Syntax

```python
Elements.is_empty() -> bool
```

## Usage

{% code title="correct usage" %}
```python
py.find("a.hidden-link").is_empty()
```
{% endcode %}

{% code title="incorrect usage" %}
```python
# Errors, 'Element' is not a list
py.get("a").is_empty()
```
{% endcode %}

## Arguments

* None

## Yields

* **bool** - True if the length is zero, else False
