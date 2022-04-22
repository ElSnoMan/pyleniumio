---
description: This property get the size of the current window.
---

# window\_size

## Syntax

```python
py.window_size -> Dict[str, int]
```

## Usage

{% code title="correct usage" %}
```python
size = py.window_size

# print the width
print(size["width"])

# print the height
print(size["height"]
```
{% endcode %}

## Arguments

* None

## Yields

* <mark style="color:orange;">**Dict\[str, int]**</mark> - The current window's size as a dictionary
