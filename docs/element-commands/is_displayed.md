---
description: The command to check if this element is displayed.
---

# is\_displayed

## Syntax

```python
Element.is_displayed()
```

## Usage

{% code title="correct usage" %}
```python
py.get('#button').is_displayed()
```
{% endcode %}

## Arguments

* None

## Yields

* **(bool)** True if the element is displayed, else False

{% hint style="info" %}
"displayed" means that the element is in the DOM and has a size greater than zero such that it is visible to the user.
{% endhint %}
