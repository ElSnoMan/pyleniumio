---
description: The command to get DOM elements that match the XPath selector.
---

# \(deprecated\) xpath

{% hint style="danger" %}
This is no longer valid in version 1.8.0+
{% endhint %}

## Syntax

```python
py.xpath(xpath)
py.xpath(xpath, at_least_one)
py.xpath(xpath, timeout)
py.xpath(xpath, at_least_one, timeout)

---or---

Element.xpath(xpath)
Element.xpath(xpath, at_least_one)
Element.xpath(xpath, timeout)
Element.xpath(xpath, at_least_one, timeout)
```

## Usage

{% code title="correct usage" %}
```python
# Yield Elements in .nav with tag name of a
py.get('.nav').xpath('//a')

---or---

# Yield Elements in document with id of 'button'
py.xpath('//*[@id="button"]')

---or--- # store in variable

element = py.xpath('//*[@id="button"]')

---or--- # chain an Element(s) command

# if one element is found
py.xpath('//*[@id="button"]').click()

# if more elements are found
py.xpath('//*[@id="button"]').first().click()

---or--- # control the timeout in any of the above usages

py.xpath('//a[@href="/about"]', timeout=5).click()
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
* `at_least_one=True (bool)` - **True** if you want to wait for at least one element to be found
* `timeout=0 (int)` - The amount of seconds for this command to succeed.
  * This overrides the **default** **wait\_time** in `pylenium.json()`

## Yields

* **\(Elements\)** A list of the found elements. If only one is found, return **Element** instead.

## Examples

```python
# if you expect the elements not to be present
elements = py.xpath('//a', at_least_one=False)

# otherwise, just use the default
elements = py.xpath('//a')
```

