---
description: The command to switch the driver's context to the given element.
---

# frame\_by\_element

## Syntax

```python
py.switch_to.frame_by_element(element: Element, timeout: int = 0) -> Pylenium
```

## Usage

{% code title="correct usage" %}
```python
iframe = py.get("iframe")
py.switch_to.frame_by_element(iframe)

---or--- # chain a Pylenium command

iframe = py.get("iframe")
py.switch_to.frame_by_element(iframe).contains("Add New").click()
```
{% endcode %}

## Arguments

* <mark style="color:purple;">`element (Element)`</mark> - The <mark style="color:orange;">**Element**</mark> to switch to
* <mark style="color:purple;">`timeout=0 (int)`</mark> - The number of seconds to wait for the frame to be switched to

## Yields

* <mark style="color:orange;">**Pylenium**</mark> - The current instance of Pylenium so you can chain commands

## Examples

```html
<div>
    <frame id='foo'>
        <a href='/different-page' id='bar'>Link in iframe</a>
    </frame>
</div>
```

If we wanted to click the link above, we would need to:

1. Switch the driver's context to the iframe
2. Then perform the click

This is a piece of cake with Pylenium:

```python
iframe = py.get("#foo")
py.switch_to.frame_by_element(iframe).get("#bar").click()
```
