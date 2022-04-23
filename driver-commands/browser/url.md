---
description: The command to get the current page's URL.
---

# url

## Syntax

```python
py.url() -> str
```

## Usage

{% code title="correct usage" %}
```
py.url()
```
{% endcode %}

{% code title="incorrect usage" %}
```
py.url
```
{% endcode %}

## Arguments

* None

## Yields

* <mark style="color:orange;">**str**</mark> - The current page's URL

## Examples

```python
assert py.url().endswith("/checkout")
```
