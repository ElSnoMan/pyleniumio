---
description: The command to get the current page's URL.
---

# url

## Syntax

```text
py.url()
```

## Usage

{% code title="correct usage" %}
```text
py.url()
```
{% endcode %}

{% code title="incorrect usage" %}
```text
py.url
```
{% endcode %}

## Arguments

* None

## Yields

* **\(str\)** The current page's URL

## Examples

```python
assert py.url().endswith('/checkout')
```

