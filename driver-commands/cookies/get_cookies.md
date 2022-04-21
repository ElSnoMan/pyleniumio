---
description: The command to get all cookies in the current browser session.
---

# get\_cookies

## Syntax

```python
py.get_cookies() -> List[Dict]
```

## Usage

{% code title="correct usage" %}
```python
py.get_cookies()

---or--- # store in a variable

cookies = py.get_cookies()
```
{% endcode %}

## Arguments

* None

## Yields

* <mark style="color:purple;">**`List[Dict]`**</mark> A list of cookie objects. Each cookie object has the following properties:
  * `name`
  * `value`
  * `path`
  * `domain`
  * `httpOnly`
  * `secure`
  * `expiry`

## Examples

```python
py.set_cookie({"name": "foo", "value": "bar"})

cookie = py.get_cookies()[0]

print(cookie["name"])      # "foo"
print(cookie.get("value")) # "bar"
```

```python
py.set_cookie({"name": "foo", "value": "bar"})
py.set_cookie({"name": "yes", "value", "please"})

for cookie in py.get_cookies():
    print(cookie["name"])
    print(cookie.get("value"))
```
