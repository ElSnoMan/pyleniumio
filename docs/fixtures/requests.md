---
description: A library for working with HTTP Clients and APIs.
---

# ↗️ api

## What is requests?

<mark style="color:orange;">**Requests**</mark> is an elegant and simple HTTP library for Python, built for human beings.

{% embed url="https://requests.readthedocs.io/en/latest/" %}
requests official documentation
{% endembed %}

## Two Ways to Use it

* `api fixture` - A fixture of **requests** for any tests
* `import requests` - Simply use the import statement to bring it into any file!

## Syntax

```python
def test_(api)

---or--- # just import it

# recommended
import requests
```

## Usage

{% code title="api fixture" %}
```python
def test_api_fixture(api):
    response = api.get(f"{BASE_URL}/api/cards")
```
{% endcode %}

{% code title="Recommended" %}
```python
import requests

response = requests.get(f"{BASE_URL}/api/cards")
```
{% endcode %}

## CRUD

Requests provides everything you need out of the box, but these are probably the actions you want :)

### GET

```python
requests.get()
```

### POST

```python
requests.post()
```

### DELETE

```python
requests.delete()
```

### PATCH

```python
requests.patch()
```

### PUT

```python
requests.put()
```
