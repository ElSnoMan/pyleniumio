---
description: The command to get the cookie with the given name.
---

# get\_cookie

## Syntax

```python
py.get_cookie(name)
```

## Usage

{% code title="correct usage" %}
```python
py.get_cookie('foo')

---or--- # "key" into the dictionary

val = py.get_cookie('foo')['value']

---or--- # use the .get() function in dict

val = py.get_cookie('foo').get('value')
```
{% endcode %}

## Arguments

* `name (str)` - The name of the cookie

## Yields

* **\(dict\)** The cookie as a dictionary. Cookie objects have the following properties:
  * `name`
  * `value`
  * `path`
  * `domain`
  * `httpOnly`
  * `secure`
  * `expiry`

{% hint style="info" %}
Returns **None** if the cookie does not exist
{% endhint %}

