---
description: Navigate forward or back in the browser's history.
---

# go

## Syntax

```python
py.go(direction)
py.go(direction, number)
```

## Usage

* Go forward one page

```python
py.go('forward')
```

* Go back two pages

```python
py.go('back', 2)
```

## Arguments

* `direction (str)` - forward or back
* `number=1 (int)` - go back or forward N pages in history

{% hint style="warning" %}
**`number`** must be a positive integer.
{% endhint %}

## Yields

* **(Pylenium)** The current instance of Pylenium so you can chain commands.
