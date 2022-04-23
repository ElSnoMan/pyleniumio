---
description: The command to open a new browser tab and switch to it.
---

# new\_tab

## Syntax

```python
py.switch_to.new_tab() -> Pylenium
```

## Usage

{% code title="correct usage" %}
```python
# Open a new window and hold it in a variable
tab = py.switch_to.new_tab()

---or---

# Open a new window and chain a command
py.switch_to.new_tab().visit("https://qap.dev")
```
{% endcode %}

## Arguments

* None

## Yields

* <mark style="color:orange;">**Pylenium**</mark> - The current instance of Pylenium so you can chain commands in the new tab
