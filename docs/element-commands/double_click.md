---
description: The command to double click the element.
---

# double\_click

## Syntax

```python
Element.double_click()
```

## Usage

{% code title="correct usage" %}
```python
py.get('a').double_click()

---or--- # chain a Pylenium command

py.get('a').double_click().switch_to.window(index=1)
```
{% endcode %}

{% code title="incorrect usage" %}
```python
# Errors, 'double_click' yields Pylenium, not Element
py.get('a').double_click().text
```
{% endcode %}

## Arguments

* None

## Yields

* **\(Pylenium\)** The current instance of Pylenium so you can chain commands

