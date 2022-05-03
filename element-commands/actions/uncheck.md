---
description: The command to deselect checkboxes and radio buttons.
---

# uncheck

## Syntax

```python
Element.uncheck() -> Element
Element.uncheck(allow_selected=False) -> Element
```

## Usage

{% code title="correct usage" %}
```python
# uncheck a radio button
py.get("[type='radio']").uncheck()
```
{% endcode %}

{% code title="incorrect usage" %}
```python
# Errors, 'get' yields an Element that is not a checkbox or radio button
py.get("a").uncheck()
```
{% endcode %}

## Arguments

* <mark style="color:purple;">`allow_deselected=False (bool)`</mark> - If **True,** do not raise an error if the box or radio button to uncheck is _already_ deselected.

{% hint style="info" %}
Default is **False** because why would you want to deselect a box that's not selected?
{% endhint %}

## Yields

* <mark style="color:orange;">**Element**</mark> - The current Element so you can chain commands

## Raises

* <mark style="color:yellow;">**ValueError**</mark> if the element is not selected already. Set `allow_deselected` to **True** to ignore this.
* <mark style="color:yellow;">**ValueError**</mark> if the element is not a checkbox or radio button

## Examples

Given this HTML:

```html
<form id="checkboxes">
    <input type="checkbox">
    checkbox 1
    <br>
    <input type="checkbox" checked="">
    checkbox 2
  </form>
```

We can _uncheck_ the second checkbox:

```python
def test_uncheck(py: Pylenium):
    py.visit("https://the-internet.herokuapp.com/checkboxes")
    checkboxes = py.find("input")
    second_box = checkboxes[1].uncheck()
    assert second_box.is_checked() is False
```
