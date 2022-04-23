---
description: The command to open a new browser window and switch to it.
---

# new\_window

## Syntax

```python
py.switch_to.new_window() -> Pylenium
```

## Usage

{% code title="correct usage" %}
```python
# Open a new window and hold it in a variable
window = py.switch_to.new_window()

---or---

# Open a new window and chain a command
py.switch_to.new_window().visit("https://qap.dev")
```
{% endcode %}

## Arguments

* None

{% hint style="info" %}
**index=0** will switch to the default content
{% endhint %}

## Yields

* <mark style="color:orange;">**Pylenium**</mark> - The current instance of Pylenium so you can chain commands in the new window
