---
description: The command to get a single Element that matches the CSS selector.
---

# get

## Syntax

```python
py.get(css: str) -> Element
py.get(css: str, timeout: int) -> Element

---or---

Element.get(css: str) -> Element
Element.get(css: str, timeout: int) -> Element
```

## Usage

{% code title="correct usage" %}
```python
# Yield Element in .nav with tag name of a
py.get(".nav").get("a")

---or---

# Yield first Element in the DOM with id of 'button'
py.get("#button")

---or--- # store in a variable

element = py.get("#login")

---or--- # chain an Element command

py.get("#save-button").click()

---or--- # control the timeout in any of the above usages

py.get("a[href='/about']", timeout=5).click()
```
{% endcode %}

{% code title="incorrect usage" %}
```python
# Errors, 'title' does not yield Element
py.title.get("QAP")

---or---

# Errors, 'get_cookie' does not yield Element
py.get_cookie().get("Cooke Monster")
```
{% endcode %}

## Arguments

* `css (str)` - The CSS selector to use
* `timeout=None (int)` - The number of seconds for this command to succeed.
  * <mark style="color:purple;">`timeout=None`</mark> will use the default <mark style="color:orange;">**wait\_time**</mark>** ** in [pylenium.json](../../docs/configuration/pylenium.json.md)
  * <mark style="color:purple;">`timeout=0`</mark> will poll the DOM immediately with no wait
  * Greater than zero will _override_ the default <mark style="color:orange;">**wait\_time**</mark>

## Yields

* <mark style="color:orange;">**Element**</mark> - The first element that is found, even if multiple elements match the query.
