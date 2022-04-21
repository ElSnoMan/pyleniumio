---
description: Pylenium offers many commands and features out of the box.
---

# Overview

## py

This is the main object in Pylenium. This is essentially the **Bot or Browser** you're controlling in your tests. Navigate to websites, take screenshots, find elements to click on or enter text, and much more!

{% code title="example" %}
```python
from pylenium.driver import Pylenium


def test_visit(py: Pylenium):
    py.visit("https://qap.dev")
```
{% endcode %}

## Element and Elements

These commands allow you to interact and perform actions against an [Element](../element-commands/) or [Elements](../elements-commands/).

{% code title="Chain commands" %}
```python
py.get("ul").find("li").first().click()
```
{% endcode %}

{% code title="or use variables" %}
```bash
# Click the first element with id=button
element = py.get("#button")
element.click()
```
{% endcode %}

{% code title="Mix and match variables and chains" %}
```python
# Print the href value of all links on the page
elements = py.find("a")
for el in elements:
    print(el.get_attribute("href"))
```
{% endcode %}

{% code title="Use what is best for you :)" %}
```python
# Check all checkboxes
py.find("input.checkbox").check()
```
{% endcode %}
