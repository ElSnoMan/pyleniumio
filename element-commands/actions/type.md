---
description: The command to type keys into a field, input or text box.
---

# type

{% hint style="info" %}
Replaces **`send_keys`** from Selenium
{% endhint %}

## Syntax

```python
Element.type(*args) -> Element
```

## Usage

{% code title="correct usage" %}
```python
py.get("#username").type("my-username")

---or--- # combine with other keys and strings

# import the Keys from selenium
py.get("#search").type("puppies", Keys.ENTER)

---or--- # chain an Element command

py.get("#email").type("foo@example.com").get_attribute("value")
```
{% endcode %}

{% code title="incorrect usage" %}
```python
# Errors, 'type' may have no effect on other types of elements
py.get("a").type("foo")
```
{% endcode %}

## Arguments

* <mark style="color:purple;">`*args (Any)`</mark> - A comma-separated list of arguments to type

{% hint style="success" %}
It's best to use **strings** and the **Keys** from Selenium
{% endhint %}

## Yields

* <mark style="color:orange;">**Element**</mark> - The current Element so you can chain commands

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
