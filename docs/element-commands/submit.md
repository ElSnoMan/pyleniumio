---
description: The command to submit a form.
---

# submit

## Syntax

```python
Element.submit()
```

## Usage

{% code title="correct usage" %}
```python
py.get('form').submit()

---or---

py.get('input[type="submit"]').submit()
```
{% endcode %}

{% code title="incorrect usage" %}
```python
# Errors, 'submit' may have no effect on certain elements
py.get('a').submit()
```
{% endcode %}

## Arguments

* None

## Yields

* **\(Pylenium\)** The current instance of Pylenium so you can chain commands.

{% hint style="info" %}
You can continue the chain if `.submit()` opens a new view or navigates to a different page
{% endhint %}

