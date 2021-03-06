---
description: The command to find all the elements that match the XPath selector.
---

# findx

## Syntax

```python
py.findx(xpath)
py.findx(xpath, timeout)

---or---

Element.findx(xpath)
Element.findx(xpath, timeout)
```

## Usage

{% code title="correct usage" %}
```python
# Yield all Elements in .nav with tag name of a
py.get('.nav').findx('//a')

---or---

# Yield all Elements in document with id of 'button'
py.findx('//*[@id="button"]')

---or--- # store in variable

elements = py.findx('//*[@id="button"]')

---or--- # chain an Element(s) command

# if one element is found, still returns a list of 1: [Element]
py.findx('//*[@id="button"]').first().click()

---or--- # control the timeout in any of the above usages

py.findx('//a[@href="/about"]', timeout=5).length()
```
{% endcode %}

{% code title="incorrect usage" %}
```python
# Errors, 'title' does not yield Element
py.title.findx('//a')

---or---

# Errors, 'get_cookie' does not yield Element
py.get_cookie().findx('//[text()="foo" and @class="bar"]')
```
{% endcode %}

## Arguments

* `xpath (str)` - The XPATH selector to use
* `timeout=None (int)` - The amount of seconds for this command to succeed.
  * `None` will use the default **wait\_time** in `pylenium.json`
  * Zero \(`0`\) will poll the DOM immediately with no wait
  * Greater than zero will override the default **wait\_time**

## Yields

* **\(Elements\)** The list of elements found.
  * If none are found, returns an empty list
  * If one or more are found, return the list normally

## Examples

```python
# there should be 3 `a` elements
py.findx('//a').should().have_length(3)
```

