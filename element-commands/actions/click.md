---
description: The command to click the element.
---

# click

## Syntax

```python
Element.click() -> Pylenium
Element.click(force=False) -> Pylenium
```

## Usage

{% code title="correct usage" %}
```python
py.get("a").click()

---or--- # chain a Pylenium command

py.get("a").click().wait.until(lambda _: py.title == "New Page")
```
{% endcode %}

{% code title="incorrect usage" %}
```python
# Errors, 'click' yields Pylenium, not Element
py.get("a").click().text()
```
{% endcode %}

## Arguments

* <mark style="color:purple;">`force=False (bool)`</mark> - If **True**, a JavascriptExecutor command is sent instead of Selenium's native `.click()`

## Yields

* <mark style="color:orange;">**Pylenium**</mark> - The current instance of Pylenium so you can chain commands.

## Examples

Given this HTML:

```html
<div class="example">
  <button onclick="addElement()">Add Element</button>
  <hr>
  <div id="elements">
    <button class="added-manually" onclick="deleteElement()">Delete</button></div>
</div>
```

We can click to add another element and click to delete them:

```python
URL = "https://the-internet.herokuapp.com/add_remove_elements/"
ADD_BUTTON = "[onclick='addElement()']"
DELETE_BUTTON = "[onclick='deleteElement()']"

def test_click_to_add_and_delete(py: Pylenium):
    py.visit(URL)
    py.get(ADD_BUTTON).click()
    py.get(DELETE_BUTTON).click()
    assert py.should().not_find(DELETE_BUTTON)
```

{% hint style="info" %}
Give it a try yourself! [https://the-internet.herokuapp.com/add\_remove\_elements/](https://the-internet.herokuapp.com/add\_remove\_elements/)
{% endhint %}
