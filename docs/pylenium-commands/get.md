---
description: The command to get the DOM element that matches the CSS selector.
---

# get

## Syntax

```python
py.get(css)
py.get(css, timeout)

---or---

Element.get(css)
Element.get(css, timeout)
```

## Usage

{% code title="correct usage" %}
```python
# Yield Element in .nav with tag name of a
py.get('.nav').get('a')

---or---

# Yield first Element in document with id of 'button'
py.get('#button')


---or--- # store in variable

element = py.get('#login')

---or--- # chain an Element command

py.get('#save-button').click()

---or--- # control the timeout in any of the above usages

py.get('a[href="/about"]', timeout=5).click()
```
{% endcode %}

{% code title="incorrect usage" %}
```python
# Errors, 'title' does not yield Element
py.title.get('QAP')

---or---

# Errors, 'get_cookie' does not yield Element
py.get_cookie().get('Cooke Monster')
```
{% endcode %}

## Arguments

* `css (str)` - The CSS selector to use
* `timeout=0 (int)` - The amount of seconds for this command to succeed.
  * `None` will use the default **wait\_time** in `pylenium.json`
  * Zero \(`0`\) will poll the DOM immediately with no wait
  * Greater than zero will override the default **wait\_time**

## Yields

* **\(Element\)** The first element that is found, even if multiple elements match the query.

