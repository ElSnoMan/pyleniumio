---
description: The command to navigate to URLs.
---

# visit

## Syntax

```python
py.visit(url)
```

## Usage

```bash
py.visit('https://qap.dev')
```

## Arguments

* `url (str)` - the URL to visit

{% hint style="info" %}
Make sure to include the protocol **http** or **https**
{% endhint %}

## Yields

* **(Pylenium)** The current instance of **Pylenium** so you can _chain_ another command

## Examples

```bash
# navigate to a URL
py.visit('https://qap.dev')
```

```bash
# navigate to a URL and click on About link
py.visit('https://qap.dev').contains('About').click()
```
