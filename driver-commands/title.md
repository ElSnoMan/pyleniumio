---
description: The command to get the current page's title.
---

# title

## Syntax

```python
py.title() -> str
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

* <mark style="color:orange;">**str**</mark>  - The <mark style="color:purple;">`document.title`</mark> property of the current page

## Examples

```python
assert py.title() == "QA at the Point"
```

