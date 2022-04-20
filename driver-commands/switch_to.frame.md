---
description: The command to switch the driver's context to the frame given its name or id.
---

# switch\_to.frame

## Syntax

```python
py.switch_to.frame(name_or_id)
```

## Usage

{% code title="correct usage" %}
```python
# switch to an iframe with name of 'main-content'
py.switch_to.frame('main-content')

---or--- # chain a Pylenium command

py.switch_to.frame('main-content').contains('Add New').click()
```
{% endcode %}

## Arguments

* `name_or_id (str)` - The **name** or **id** attribute value of the `<frame>` element

## Yields

* **(Pylenium)** The current instance of Pylenium so you can chain commands

## Examples

```python
<div>
    <frame id='foo'>
        <a href='/different-page' id='bar'>Link in iframe</a>
    </frame>
</div>
```

If we wanted to click the link above, we would need to:

1. switch the driver's context to the iframe
2. then perform the click

This is a piece of cake with Pylenium:

```python
py.switch_to.frame('foo').get('#bar').click()
```
