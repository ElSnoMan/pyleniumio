---
description: The command to get the length of Elements.
---

# length

## Syntax

```python
Elements.length()
```

## Usage

{% code title="correct usage" %}
```python
assert py.find('li').length() == 5

---or---

assert py.find('li').should().have_length(5)
```
{% endcode %}

{% code title="incorrect usage" %}
```python
# Errors, 'get' yields Element, not Elements
assert py.get('li').length() == 1
```
{% endcode %}

## Arguments

* None

## Yields

* **(int)** The length of the Elements
