---
description: The command to navigate to URLs.
---

# visit

## Syntax

```python
py.visit(url: str) -> Pylenium
```

## Usage

```bash
py.visit("https://qap.dev")
```

## Arguments

* <mark style="color:purple;">`url (str)`</mark> - the URL to visit

{% hint style="info" %}
Make sure to include the protocol **http** or **https**
{% endhint %}

## Yields

* <mark style="color:orange;">**Pylenium**</mark> - The current instance of **Pylenium** so you can _chain_ another command

## Examples

```bash
# Navigate to a URL
py.visit("https://qap.dev")
```

```bash
# Navigate to a URL and click on About link
py.visit("https://qap.dev").contains("About").click()
```
