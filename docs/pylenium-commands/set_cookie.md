---
description: The command to set a cookie into the current browser session.
---

# set\_cookie

## Syntax

```python
py.set_cookie(cookie)
```

## Usage

{% code title="correct usage" %}
```python
py.set_cookie({'name' : 'foo', 'value' : 'bar'})
```
{% endcode %}

{% code title="incorrect usage" %}
```python
# Errors, 'set_cookie' accepts a single argument that is a dict
py.set_cookie('foo', 'bar')

---or---

# Errors, 'set_cookie' yields None
py.set_cookie({'name' : 'foo', 'value' : 'bar'}).get('foo')
```
{% endcode %}

## Arguments

* `cookie (dict)` - A dictionary with required keys: `"name"` and `"value"`

{% hint style="info" %}
Optional keys: `"path"`, `"domain"`, `"secure"`, `"expiry"`
{% endhint %}

## Yields

* None

