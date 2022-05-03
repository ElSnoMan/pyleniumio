---
description: The command to hover the element.
---

# hover

## Syntax

```python
Element.hover() -> Pylenium
```

## Usage

{% code title="correct usage" %}
```python
py.get(".menu").hover()
```
{% endcode %}

{% code title="incorrect usage" %}
```python
# Errors, 'hover' yields Pylenium, not Element
py.get(".menu").hover().click()
```
{% endcode %}

## Arguments

* None

## Yields

* <mark style="color:orange;">**Pylenium**</mark> - The current instance of Pylenium so you can chain commands

## Examples

```python
def test_hover_shows_user_info(py: Pylenium):
    py.visit("https://the-internet.herokuapp.com/hovers")
    py.get("[alt='User Avatar']").hover()
    assert py.contains("name: user1").should().be_visible()
```

{% hint style="info" %}
Give it a try yourself! [https://the-internet.herokuapp.com/hovers](https://the-internet.herokuapp.com/hovers)
{% endhint %}
