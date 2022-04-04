---
description: The command to get the text of the current Element.
---

# text

## Syntax

```python
Element.text()
```

## Usage

{% code title="correct usage" %}
```python
assert py.get('.nav.link').text() == 'About'

---or---

assert py.get('.nav.link').should().have_text('About')
```
{% endcode %}

{% code title="incorrect usage" %}
```python
# Errors, 'text' is not a property
py.get('a').text
```
{% endcode %}

## Arguments

* None

## Yields

* **(str)** The text of the current Element
