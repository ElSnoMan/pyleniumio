---
description: The command to get a list of Elements that match the CSS selector.
---

# find

## Syntax

```python
py.find(css: str) -> Elements
py.find(css: str, timeout: int) -> Elements

---or---

Element.find(css: str) -> Elements
Element.find(css: str, timeout: int) -> Elements
```

## Usage

{% code title="correct usage" %}
```python
# Yield Elements in .nav with tag name of a
py.get(".nav").find("a")

---or---

# Yield all Elements in the DOM with id of 'button'
py.find("#button")

---or--- # store in a variable

elements = py.find("li")

---or--- # chain an Elements command

element = py.find("ul > li").first()

---or--- # control the timeout in any of the above usages

py.find("li", timeout=5).last()
```
{% endcode %}

{% code title="incorrect usage" %}
```python
# Errors, 'title' does not yield Element
py.title.find("QAP")

---or---

# Errors, 'get_cookie' does not yield Element
py.get_cookie().find("Cooke Monster")
```
{% endcode %}

## Arguments

* `css (str)` - The CSS selector to use
* `timeout=None (int)` - The number of seconds for this command to succeed.
  * <mark style="color:purple;">`timeout=None`</mark> will use the default <mark style="color:orange;">**wait\_time**</mark> in [pylenium.json](../../docs/configuration/pylenium.json.md)
  * <mark style="color:purple;">`timeout=0`</mark> will poll the DOM immediately with no wait
  * Greater than zero will _override_ the default <mark style="color:orange;">**wait\_time**</mark>

## Yields

* <mark style="color:orange;">**Elements**</mark> - A list of elements that match the query.

## Examples

```python
# If you expect the elements not to be present
assert py.find("ul > li").should().be_empty()

# Otherwise, just use the default
elements = py.find("ul > li")
```
