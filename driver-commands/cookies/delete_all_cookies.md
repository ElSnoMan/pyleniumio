---
description: The command to delete all cookies in the current browser session.
---

# delete\_all\_cookies

## Syntax

```python
py.delete_all_cookies() -> None
```

## Usage

{% code title="correct usage" %}
```python
py.delete_all_cookies()
```
{% endcode %}

{% code title="incorrect usage" %}
```python
# Errors, 'delete_all_cookies' yields None
py.delete_all_cookies().get_cookie()
```
{% endcode %}

## Arguments

* None

## Yields

* None
