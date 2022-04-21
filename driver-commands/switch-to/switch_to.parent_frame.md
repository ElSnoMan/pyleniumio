---
description: >-
  The command to switch the driver's context to the parent frame of the current
  frame.
---

# parent\_frame

## Syntax

```python
py.switch_to.parent_frame() -> Pylenium
```

## Usage

{% code title="correct usage" %}
```python
# Switch to a frame with name of 'iframe'
py.switch_to.frame("iframe")

# Switch back to the main website
py.switch_to.parent_frame()
```
{% endcode %}

## Arguments

* None

## Yields

* <mark style="color:orange;">**Pylenium**</mark> - The current instance of Pylenium so you can chain commands

## Examples

```html
<div>
    <frame id='foo'>
        <button>Button in iframe</button>
    </frame>
    <button id='bar'>Button in main html (aka default content)</button>
</div>
```

```python
# Switch to the iframe to click the 'Button in iframe'
py.switch_to.frame("foo").contains("Button in iframe").click()

# Switch back to the main html to click the 'bar' button
py.switch_to.parent_frame().get("#bar").click()
```
