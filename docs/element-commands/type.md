---
description: 'The command to type keys into a field, input or text box.'
---

# type

## Syntax

```python
Element.type(*args)
```

## Usage

{% code title="correct usage" %}
```python
py.get('#username').type('my-username')

---or--- # combine with other keys and strings

py.get('#search').type('puppies', py.Keys.ENTER)

---or--- # chain an Element command

py.get('#email').type('foo@example.com').get_attribute('value')
```
{% endcode %}

{% code title="incorrect usage" %}
```python
# Errors, 'type' may have no effect on other types of elements
py.get('a').type('foo')
```
{% endcode %}

## Arguments

* `*args (Any)` - A comma-separated list of arguments to type

{% hint style="success" %}
It's best to use **strings** and the **Keys** class
{% endhint %}

## Yields

* **\(Element\)** The current Element so you can chain commands

