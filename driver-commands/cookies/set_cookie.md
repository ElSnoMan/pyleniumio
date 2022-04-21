---
description: The command to set a cookie into the current browser session.
---

# set\_cookie

## Syntax

```python
py.set_cookie(cookie: dict) -> None
```

## Usage

{% code title="correct usage" %}
```python
py.set_cookie({"name" : "foo", "value" : "bar"})
```
{% endcode %}

{% code title="incorrect usage" %}
```python
# Errors, 'set_cookie' accepts a single argument that is a Dict
py.set_cookie("foo", "bar")

---or---

# Errors, 'set_cookie' yields None
py.set_cookie({"name" : "foo", "value" : "bar"}).get_cookie()
```
{% endcode %}

## Arguments

* <mark style="color:purple;">`cookie (Dict)`</mark> - A dictionary with required keys: `"name"` and `"value"`

{% hint style="info" %}
Optional keys: `"path"`, `"domain"`, `"secure"`, `"expiry"`
{% endhint %}

## Yields

* None
