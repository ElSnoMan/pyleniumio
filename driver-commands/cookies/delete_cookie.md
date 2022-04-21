---
description: The command to delete a cookie with the given name.
---

# delete\_cookie

## Syntax

```python
py.delete_cookie(name: str) -> None
```

## Usage

{% code title="correct usage" %}
```python
py.delete_cookie("foo")
```
{% endcode %}

{% code title="incorrect usage" %}
```python
# Errors, 'delete_cookie' yields None
py.delete_cookie("foo").get_cookie()
```
{% endcode %}

## Arguments

* <mark style="color:purple;">`name (str)`</mark> - The name of the cookie

## Yields

* None
