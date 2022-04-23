---
description: The command to hover the element.
---

# hover

## Syntax

```python
Element.hover()
```

## Usage

{% code title="correct usage" %}
```python
py.get('.menu').hover()
```
{% endcode %}

{% code title="incorrect usage" %}
```python
# Errors, 'hover' yields Pylenium, not Element
py.get('.menu').hover().click()
```
{% endcode %}

## Arguments

* None

## Yields

* **(Pylenium)** The current instance of Pylenium so you can chain commands

## Examples

Originally, `.hover()` returned the current Element, but most hovering scenarios revealed items that were _not_ descendants of the hovered element.

```python
py.get('.menu').hover().contains('About').click()
```
