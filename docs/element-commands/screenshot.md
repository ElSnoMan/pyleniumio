---
description: The command to take a screenshot of the element.
---

# screenshot

## Syntax

```python
Element.screenshot(filename)
```

## Usage

{% code title="correct usage" %}
```python
py.get('a[href="/about"]').screenshot('elements/about-link.png')

---or--- # chain an Element command

py.get('#save-button').screenshot('save-.png').click()
```
{% endcode %}

## Arguments

* `filename (str)` - The file path including the file name and extension like `.png`

## Yields

* **(Element)** The current instance of Element so you can chain commands
