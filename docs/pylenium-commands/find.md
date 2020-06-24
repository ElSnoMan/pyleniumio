---
description: The command to get DOM elements that match the CSS selector.
---

# find

## Syntax

```python
py.find(css)
py.find(css, timeout)

---or---

Element.find(css)
Element.find(css, timeout)
```

## Usage

{% code title="correct usage" %}
```python
# Yield Elements in .nav with tag name of a
py.get('.nav').find('a')

---or---

# Yield all Elements in document with id of 'button'
py.find('#button')

---or--- # store in variable

elements = py.find('li')

---or--- # chain an Elements command

element = py.find('ul > li').first()

---or--- # control the timeout in any of the above usages

py.find('li', timeout=5).last()
```
{% endcode %}

{% code title="incorrect usage" %}
```python
# Errors, 'title' does not yield Element
py.title.find('QAP')

---or---

# Errors, 'get_cookie' does not yield Element
py.get_cookie().find('Cooke Monster')
```
{% endcode %}

## Arguments

* `css (str)` - The CSS selector to use
* `timeout=0 (int)` - The amount of seconds for this command to succeed.
  * `None` will use the default **wait\_time** in `pylenium.json`
  * Zero \(`0`\) will poll the DOM immediately with no wait
  * Greater than zero will override the default **wait\_time**

## Yields

* **\(Elements\)** A list of elements that match the query.

## Examples

```python
# if you expect the elements not to be present
assert py.find('ul > li').should().be_empty()

# otherwise, just use the default
elements = py.find('ul > li')
```

