---
description: The command to get the current page's title.
---

# title

## Syntax

```python
py.title()
```

## Usage

{% code title="correct usage" %}
```python
py.title()
```
{% endcode %}

{% code title="incorrect usage" %}
```python
py.title
```
{% endcode %}

## Arguments

* None

## Yields

* **\(str\)** The `document.title` property of the current page

## Examples

```python
assert py.title() == 'QA at the Point'
```



