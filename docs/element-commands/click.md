---
description: The command to click the element.
---

# click

## Syntax

```python
Element.click()
Element.click(force=True)
```

## Usage

{% code title="correct usage" %}
```python
py.get('a').click()

---or--- # chain a Pylenium command

py.get('a').click().wait.until(lambda _: py.title == 'New Page')
```
{% endcode %}

{% code title="incorrect usage" %}
```python
# Errors, 'click' yields Pylenium, not Element
py.get('a').click().text
```
{% endcode %}

## Arguments

* **`force=False (bool)`** - If **True**, a JavascriptExecutor command is sent instead of Selenium's native `.click()`

## Yields

* **(Pylenium)** The current instance of Pylenium so you can chain commands.

{% hint style="info" %}
You can continue the chain if `.click()` opens a new view or navigates to a different page
{% endhint %}
