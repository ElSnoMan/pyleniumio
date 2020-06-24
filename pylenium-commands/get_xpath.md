---
description: The command to get a single element using an XPath selector.
---

# get\_xpath

## Syntax

```python
py.get_xpath(xpath)
py.get_xpath(xpath, timeout)

---or---

Element.get_xpath(xpath)
Element.get_xpath(xpath, timeout)
```

## Usage

{% code title="correct usage" %}
```python
# Yield the first Element in .nav with tag name of a
py.get('.nav').get_xpath('//a')

---or---

# Yield the first Element in document with id of 'button'
py.get_xpath('//*[@id="button"]')

---or--- # store in variable

element = py.get_xpath('//*[@id="button"]')

---or--- # chain an Element(s) command

# chain an action
py.get_xpath('//*[@id="button"]').click()

---or--- # control the timeout in any of the above usages

py.get_xpath('//a[@href="/about"]', timeout=5).click()
```
{% endcode %}

{% code title="incorrect usage" %}
```python
# Errors, 'title' does not yield Element
py.title.xpath('//a')

---or---

# Errors, 'get_cookie' does not yield Element
py.get_cookie().xpath('//[text()="foo" and @class="bar"]')
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
py.get_xpath('//*[@id="button"]').should().be_visible()
```

