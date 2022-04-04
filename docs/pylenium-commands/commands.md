---
description: Pylenium offers many commands and features out of the box.
---

# Overview

## py

This is the main object in Pylenium. This is basically the **bot** you're controlling in your tests.

{% code title="example" %}
```python
py.visit('https://qap.dev')
```
{% endcode %}

{% hint style="info" %}
&#x20;This is used to interact with the browser and find elements
{% endhint %}

## element(s)

These commands allow you to interact and perform actions against an Element or Elements.

{% code title="You can chain commands" %}
```python
py.get('ul').find('li').first().click()
```
{% endcode %}

{% code title="or you can store them in variables" %}
```bash
# click the first element with id=button
element = py.get('#button')
element.click()
```
{% endcode %}

{% code title="Mix and match variables and chains" %}
```python
# print the href value of all links on the page
elements = py.find('a')
for el in elements:
    print(el.get_attribute('href'))
```
{% endcode %}

{% code title="Use what is best for you :)" %}
```python
# check all checkboxes
py.find('input.checkbox').check()
```
{% endcode %}
