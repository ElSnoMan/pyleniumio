---
description: A library for working with HTTP Clients and APIs.
---

# api \(aka requests\)

## What is requests?

**Requests** is an elegant and simple HTTP library for Python, built for human beings.

{% embed url="https://2.python-requests.org/en/master/" %}

## Three Ways to Use it

* `py.request` - A basic **requests** instance for UI tests \(V1\)
* `api fixture` - A fixture of **requests** for any tests
* `import requests` - Simply use the import statement to bring it into any file!

## Syntax

```python
# for UI tests
py.request

---or--- # use the fixture

def test_(fake)

---or--- # just import it

import requests
```

## Usage

{% code title="py.request" %}
```python
BASE_URL = 'https://statsroyale.com'


def test_py_request(py):
    py.visit(BASE_URL)
    response = py.request.get(f'{BASE_URL}/api/cards')
    assert response.ok
    assert response.json()[0]['name'] == 'Royal Ghost'
```
{% endcode %}

{% code title="api fixture" %}
```python
def test_api_fixture(api):
    response = api.request.get(f'{BASE_URL}/api/cards')
```
{% endcode %}

{% code title="import" %}
```python
import requests

response = requests.get(f'{BASE_URL}/api/cards')
```
{% endcode %}

## CRUD

Requests provides everything you need out of the box, but these are probably the actions you want :\)

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

