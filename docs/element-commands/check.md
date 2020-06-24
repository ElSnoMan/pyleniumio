---
description: The command to select checkboxes or radio buttons.
---

# check

## Syntax

```python
Element.check()
Element.check(allow_selected)

---or---

Elements.check()
Elements.check(allow_selected)
```

## Usage

{% code title="correct usage" %}
```python
# check a radio button
py.get('[type="radio"]').check()

---or---

# check all boxes on the page
py.find('[type="checkbox"]').check()

```
{% endcode %}

{% code title="incorrect usage" %}
```python
# Errors, 'get' yields an Element that is not a checkbox or radio button
py.get('a').check()
```
{% endcode %}

## Arguments

* `allow_selected=False (bool)` - If **True,** do not raise an error if the box or radio button to check is _already_ selected.

{% hint style="info" %}
Default is **False** because why would you want to select a box that's already selected?
{% endhint %}

## Yields

* **\(Element or Elements\)** The current instance so you can chain commands

## Raises

* **ValueError** if the element is selected already. Set `allow_selected` to **True** to ignore this.
* **ValueError** if the element is not a checkbox or radio button

