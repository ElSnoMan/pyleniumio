---
description: Navigate forward or back in the browser's history.
---

# go

## Syntax

```python
py.go(direction: str) -> Pylenium
py.go(direction: str, number: int) -> Pylenium
```

## Usage

* Go forward one page

```python
py.go("forward")
```

* Go back two pages

```python
py.go("back", 2)
```

## Arguments

* <mark style="color:purple;">`direction (str)`</mark> - forward or back
* <mark style="color:purple;">`number=1 (int)`</mark> - go back or forward N pages in history

{% hint style="warning" %}
**`number`** must be a positive integer.
{% endhint %}

## Yields

* <mark style="color:orange;">**Pylenium**</mark>** -** The current instance of Pylenium so you can chain commands.
