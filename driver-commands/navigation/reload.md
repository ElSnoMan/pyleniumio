---
description: The command to reload or "refresh" the current page
---

# reload

## Syntax

```python
py.reload() -> Pylenium
```

## Usage

```python
py.reload()
```

## Arguments

* None

## Yields

* <mark style="color:orange;">**Pylenium**</mark> - The current instance of **Pylenium** so you can _chain_ another command

## Examples

```python
# Reload the page and click on the About link
py.reload().contains("About").click()
```

&#x20;
