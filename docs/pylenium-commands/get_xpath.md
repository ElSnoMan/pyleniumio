---
description: The command to get a single element using an XPath selector.
---

# getx

## Syntax

```python
py.getx(xpath)
py.getx(xpath, timeout)

---or---

Element.getx(xpath)
Element.getx(xpath, timeout)
```

## Usage

{% code title="correct usage" %}
```python
# Yield the first Element in .nav with tag name of a
py.get('.nav').getx('//a')

---or---

# Yield the first Element in document with id of 'button'
py.getx('//*[@id="button"]')

---or--- # store in variable

element = py.getx('//*[@id="button"]')

---or--- # chain an Element(s) command

# chain an action
py.getx('//*[@id="button"]').click()

---or--- # control the timeout in any of the above usages

py.getx('//a[@href="/about"]', timeout=5).click()
```
{% endcode %}

{% code title="incorrect usage" %}
```python
# Errors, 'title' does not yield Element
py.title.getx('//a')

---or---

# Errors, 'get_cookie' does not yield Element
py.get_cookie().getx('//[text()="foo" and @class="bar"]')
```
{% endcode %}

## Arguments

* `xpath (str)` - The XPATH selector to use
* `timeout=None (int)` - The amount of seconds for this command to succeed.
  * `None` will use the default **wait\_time** in `pylenium.json`
  * Zero \(`0`\) will poll the DOM immediately with no wait
  * Greater than zero will override the default **wait\_time**

## Yields

* **\(Element\)** The first element found, even if multiple elements match the query.

## Examples

```python
# the button should be displayed
py.getx('//*[@id="button"]').should().be_visible()
```

