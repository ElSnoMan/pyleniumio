---
description: The command to select a checkbox or radio buttons.
---

# check

## Syntax

```python
Element.check() -> Element
Element.check(allow_selected=False) -> Element
```

## Usage

{% code title="correct usage" %}
```python
# check a radio button
py.get("[type='radio']").check()

---or---

# check a box
py.get("[type='checkbox']").check()
```
{% endcode %}

{% code title="incorrect usage" %}
```python
# Errors, 'get' yields an Element that is not a checkbox or radio button
py.get("a").check()
```
{% endcode %}

## Arguments

* <mark style="color:purple;">`allow_selected=False (bool)`</mark> - If **True,** do not raise an error if the box or radio button to check is _already_ selected.

{% hint style="info" %}
Default is **False** because why would you want to select a box that's already selected?
{% endhint %}

## Yields

* <mark style="color:orange;">**Element**</mark>** ** - The current instance so you can chain commands

## Raises

* <mark style="color:yellow;">**ValueError**</mark> if the element is selected already. Set `allow_selected` to **True** to ignore this.
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

We can _check_ the first checkbox:

```python
def test_check_the_box(py: Pylenium):
    py.visit("https://the-internet.herokuapp.com/checkboxes")
    checkbox = py.get("input").check()
    assert checkbox.should().be_checked()
```
