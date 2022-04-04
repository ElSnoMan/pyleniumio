---
description: >-
  The property that is the current instance of Selenium's WebElement that
  Element is wrapping.
---

# webelement

## Syntax

```python
Element.webelement
```

## Usage

{% code title="correct usage" %}
```python
py.get('a').webelement
```
{% endcode %}

{% code title="incorrect usage" %}
```python
# Errors, 'webelement' is not a function
py.get('a').webelement()
```
{% endcode %}

## Arguments

* None

## Yields

* **(WebElement)** The current instance of Selenium's **WebElement** that is wrapped by **Element**

## Examples

Most scenarios won't need this, but it's provided just in case. The biggest reasons to use `.webelement`

* access functionality that may not exist in Pylenium
* functionality that requires you pass in a WebElement

```python
# Using the expected_conditions as EC
element = py.get('.loading-spinner')
py.wait.until(EC.staleness_of(element.webelement))
```
