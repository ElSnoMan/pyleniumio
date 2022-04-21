---
description: The command to get a list of Elements that match the XPath selector.
---

# findx

## Syntax

```python
py.findx(xpath: str) -> Elements
py.findx(xpath: str, timeout: int) -> Elements

---or---

Element.findx(xpath: str) -> Elements
Element.findx(xpath: str, timeout: int) -> Elements
```

## Usage

{% code title="correct usage" %}
```python
# Yield all Elements in .nav with tag name of a
py.get(".nav").findx("//a")

---or---

# Yield all Elements in document with id of 'button'
py.findx("//*[@id='button']")

---or--- # store in a variable

elements = py.findx("//*[@id='button']")

---or--- # chain an Element(s) command

# if one element is found, still returns a list of 1: [Element]
py.findx("//*[@id='button']").first().click()

---or--- # control the timeout in any of the above usages

py.findx("//a[@href='/about']", timeout=5).length()
```
{% endcode %}

{% code title="incorrect usage" %}
```python
# Errors, 'title' does not yield Element
py.title().findx("//a")

---or---

# Errors, 'get_cookie' does not yield Element
py.get_cookie().findx("//[text()='foo' and @class='bar']")
```
{% endcode %}

## Arguments

* `xpath (str)` - The XPATH selector to use
* `timeout=None (int)` - The number of seconds for this command to succeed.
  * <mark style="color:purple;">`timeout=None`</mark> will use the default <mark style="color:orange;">**wait\_time**</mark>** ** in [pylenium.json](../../docs/configuration/pylenium.json.md)
  * <mark style="color:purple;">`timeout=0`</mark> will poll the DOM immediately with no wait
  * Greater than zero will _override_ the default <mark style="color:orange;">**wait\_time**</mark>

## Yields

* <mark style="color:orange;">**Elements**</mark>** -** The list of elements found.
  * If none are found, returns an empty list
  * If one or more are found, return the list normally

## Examples

```python
# There should be 3 `a` elements
py.findx("//a").should().have_length(3)
```
