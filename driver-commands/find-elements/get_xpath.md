---
description: The command to get a single Element using an XPath selector.
---

# getx

## Syntax

```python
py.getx(xpath: str) -> Element
py.getx(xpath: str, timeout: int) -> Element

---or---

Element.getx(xpath: str) -> Element
Element.getx(xpath: str, timeout: int) -> Element
```

## Usage

{% code title="correct usage" %}
```python
# Yield the first Element in .nav with tag name of a
py.get(".nav").getx("//a")

---or---

# Yield the first Element in document with id of 'button'
py.getx("//*[@id='button']")

---or--- # store in a variable

element = py.getx("//*[@id='button']")

---or--- # chain an Element(s) command

# chain an action
py.getx("//*[@id='button']").click()

---or--- # control the timeout in any of the above usages

py.getx("//a[@href='/about']", timeout=5).click()
```
{% endcode %}

{% code title="incorrect usage" %}
```python
# Errors, 'title' does not yield Element
py.title.getx("//a")

---or---

# Errors, 'get_cookie' does not yield Element
py.get_cookie().getx("//[text()='foo' and @class='bar']")
```
{% endcode %}

## Arguments

* `xpath (str)` - The XPATH selector to use
* `timeout=None (int)` - The number of seconds for this command to succeed.
  * <mark style="color:purple;">`timeout=None`</mark> will use the default <mark style="color:orange;">**wait\_time**</mark>** ** in [pylenium.json](../../docs/configuration/pylenium.json.md)
  * <mark style="color:purple;">`timeout=0`</mark> will poll the DOM immediately with no wait
  * Greater than zero will override the default <mark style="color:orange;">**wait\_time**</mark>

## Yields

* <mark style="color:orange;">**Element**</mark> - The first element found, even if multiple elements match the query.

## Examples

```python
# The button should be displayed
py.getx("//*[@id='button']").should().be_visible()
```
