---
description: The command to take a screenshot of the current window.
---

# screenshot

## Syntax

```python
py.screenshot(filename)
```

## Usage

{% code title="correct usage" %}
```python
# saves the screenshot to the current working directory
py.screenshot('ss.png')

---or---

# saves the screenshot using the filepath
py.screenshot('../images/ss.png')
```
{% endcode %}

{% code title="incorrect usage" %}
```python
# Errors, include the file extension like '.png'
py.screenshot('ss')

---or---

# Errors, .screenshot() yields None
py.screenshot('ss.png').get('a')
```
{% endcode %}

## Arguments

* `filename (str)` - The filename including the **path** to the directory you want to save it in

{% hint style="info" %}
Make sure to include the file extension like **.png**
{% endhint %}

## Yields

* None
