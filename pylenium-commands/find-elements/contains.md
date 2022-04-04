---
description: The command to get a single Element containing the given text.
---

# contains

## Syntax

```python
py.contains(text)
py.contains(text, timeout)

---or---

Element.contains(text)
Element.contains(timeout)
```

## Usage

{% code title="correct usage" %}
```python
# Yield Element in .nav containing 'About'
py.get('.nav').contains('About')

---or---

# Yield first Element in document containing 'Hello'
py.contains('Hello')

---or--- # store in variable

element = py.contains('About')

---or--- # chain an Element command

py.contains('About').click()

---or--- # control the timeout in any of the above usages

py.contains('Deck Builder', timeout=5).click()
```
{% endcode %}

{% code title="incorrect usage" %}
```python
# Errors, 'title' does not yield Element
py.title().contains('QAP')

---or---

# Errors, 'get_cookies' does not yield Element
py.get_cookies().contains('Cooke Monster')
```
{% endcode %}

## Arguments

* `text (str)` - The text to look for
* `timeout=0 (int)` - The number of seconds for this command to succeed.
  * `None` will use the default **wait\_time** in `pylenium.json`
  * Zero (`0`) will poll the DOM immediately with no wait
  * Greater than zero will override the default **wait\_time**

{% hint style="info" %}
It does not need to be an _exact_ match
{% endhint %}

## Yields

* **(Element)** The first element that is found, even if multiple elements match the query
