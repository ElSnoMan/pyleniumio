---
description: The command to deselect checkboxes and radio buttons.
---

# uncheck

## Syntax

```python
Element.uncheck()
Element.uncheck(allow_selected)

---or---

Elements.uncheck()
Elements.uncheck(allow_selected)
```

## Usage

{% code title="correct usage" %}
```python
# uncheck a radio button
py.get('[type="radio"]').uncheck()

---or---

# uncheck all boxes on the page
py.find('[type="checkbox"]').uncheck()

```
{% endcode %}

{% code title="incorrect usage" %}
```python
# Errors, 'get' yields an Element that is not a checkbox or radio button
py.get('a').uncheck()
```
{% endcode %}

## Arguments

* `allow_deselected=False (bool)` - If **True,** do not raise an error if the box or radio button to uncheck is _already_ deselected.

{% hint style="info" %}
Default is **False** because why would you want to deselect a box that's not selected?
{% endhint %}

## Yields

* **(Element or Elements)** The current instance so you can chain commands

## Raises

* **ValueError** if the element is not selected already. Set `allow_deselected` to **True** to ignore this.
* **ValueError** if the element is not a checkbox or radio button
