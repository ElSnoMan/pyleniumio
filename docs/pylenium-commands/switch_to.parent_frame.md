---
description: >-
  The command to switch the driver's context to the parent frame of the current
  frame.
---

# switch\_to.parent\_frame

## Syntax

```python
py.switch_to.parent_frame()
```

## Usage

{% code title="correct usage" %}
```python
# switch to a frame with name of 'iframe'
py.switch_to.frame('iframe')

# switch back to the main website
py.switch_to.parent_frame()
```
{% endcode %}

## Arguments

* None

## Yields

* **\(Pylenium\)** The current instance of Pylenium so you can chain commands

## Examples

```python
<div>
    <frame id='foo'>
        <button>Button in iframe</button>
    </frame>
    <button id='bar'>Button in main html (aka default content)</button>
</div>
```

```python
# switch to the iframe to click the 'Button in iframe'
py.switch_to.frame('foo').contains('Button in iframe').click()

# switch back to the main html to click the 'bar' button
py.switch_to.parent_frame().get('#bar').click()
```

