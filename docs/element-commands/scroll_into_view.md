---
description: The command to scroll this element into the viewport
---

# scroll\_into\_view

## Syntax

```
Element.scroll_into_view()
```

## Usage

{% code title="correct usage" %}
```python
py.get('#footer-link').scroll_into_view()
```
{% endcode %}

{% code title="incorrect usage" %}
```python
# 'py' does not have this command
py.scroll_into_view()
```
{% endcode %}

## Arguments

* None

## Yields

* **(Element)** so you can chain another command
