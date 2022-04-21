---
description: >-
  The command to switch the driver's context to the default (or starting)
  content.
---

# default\_content

## Syntax

```python
py.switch_to.default_content() -> Pylenium
```

## Usage

{% code title="correct usage" %}
```python
py.switch_to.default_content()

---or--- # chain a Pylenium command in the new context

py.switch_to.default_content().get(".link")
```
{% endcode %}

## Arguments

* None

## Yields

* <mark style="color:orange;">**Pylenium**</mark> - The current instance of Pylenium so you can chain commands

{% hint style="info" %}
If the driver is already in the default context, nothing changes
{% endhint %}
