---
description: The command to submit a form or input element.
---

# submit

## Syntax

```python
Element.submit() -> Pylenium
```

## Usage

{% code title="correct usage" %}
```python
py.get("form").submit()

---or---

py.get("input[type='submit']").submit()
```
{% endcode %}

{% code title="incorrect usage" %}
```python
# Errors, 'submit' may have no effect on certain elements
py.get("a").submit()
```
{% endcode %}

## Arguments

* None

## Yields

* <mark style="color:orange;">**Pylenium**</mark> - The current instance of Pylenium so you can chain commands.

## Examples

Given this HTML:

```html
<form name="login" id="login" action="/authenticate" method="post">
    <div class="row">
      <div class="large-6 small-12 columns">
        <label for="username">Username</label>
        <input type="text" name="username" id="username">
      </div>
    </div>
    <div class="row">
      <div class="large-6 small-12 columns">
        <label for="password">Password</label>
        <input type="password" name="password" id="password">
      </div>
    </div>
      <button class="radius" type="submit"><i class="fa fa-2x fa-sign-in"> Login</i></button>
</form>
```

We could type credentials into the fields and submit the form to login:

```python
def test_login(py: Pylenium):
    py.visit("https://the-internet.herokuapp.com/login")
    py.get("#username").type("tomsmith")
    py.get("#password").type("SuperSecretPassword!")
    py.get("button[type='submit']").submit()
    assert py.contains("You logged into a secure area!").should().be_visible()
```
