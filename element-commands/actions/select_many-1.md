---
description: >-
  The command to select an <option> by its value within a <select> dropdown
  element.
---

# select\_by\_value

## Syntax

```python
Element.select_by_value(value: Any) -> Element
```

## Usage

{% code title="correct usage" %}
```python
py.get("#dropdown").select_by_value(2)

---or--- # chain an Element command

py.get("#dropdown").select_by_value("1").get_attribute("value")
```
{% endcode %}

{% code title="incorrect usage" %}
```python
# Errors, can only perform this command on a <select> dropdown element
py.get("ul > li").select_by_value("2")
```
{% endcode %}

## Arguments

* <mark style="color:purple;">`value (Any)`</mark> - The **value** of the option to select. Usually a `str`, but can be other types.

## Yields

* <mark style="color:orange;">**Element**</mark> - The current instance of Element so you can chain commands.

## Examples

Given this HTML

```html
<select id="dropdown">
    <option value="" disabled="disabled" selected="selected">Please select an option</option>
    <option value="1">Option 1</option>
    <option value="2">Option 2</option>
</select>
```

We can select any of the options

```python
dropdown = py.get("dropdown")

# Select the first option that is "disabled"
dropdown.select_by_value("")

# Select Option 1
dropdown.select_by_value("1")

# Select Option 2
dropdown.select_by_value("2")
```

{% hint style="info" %}
Give this a try yourself! [https://the-internet.herokuapp.com/dropdown](https://the-internet.herokuapp.com/dropdown)
{% endhint %}

## See also

* [select\__by\__index](select.md)&#x20;
* [select\__by\__text](select\_many.md)
* [click()](click.md) - If the dropdown is NOT a \<select> element, <mark style="color:purple;">`.click()`</mark> will work
