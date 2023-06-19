---
description: An instance of Pylenium for a Test Class
---

# ☑ pyc

## Usage

The <mark style="color:yellow;">**`pyc`**</mark> fixture is used if you want a single instance of Pylenium that is _<mark style="color:red;">**shared across tests**</mark>_ within a Test Class.

```python
from pylenium.driver import Pylenium

class TestSauceDemo:
    def test_land_on_products_page_after_login(self, pyc: Pylenium):
        pyc.visit("https://www.saucedemo.com/")
        pyc.get("#user-name").type("standard_user")
        pyc.get("#password").type("secret_sauce")
        pyc.get("#login-button").click()
        assert pyc.contains("Products").should().be_visible()
        
    def test_add_item_to_cart_increments_counter_by_1(self, pyc: Pylenium):
        pyc.get("[id*='add-to-cart']").click()
        assert pyc.get("a.shopping_cart_link").should().have_text("1")
```

{% hint style="success" %}
Import <mark style="color:yellow;">**`Pylenium`**</mark> and add the _**type hint**_ to your tests (as shown above) so you get intellisense and autocomplete when writing tests :muscle:
{% endhint %}

## Arguments

* <mark style="color:yellow;">**`none`**</mark>

## Yields

* <mark style="color:orange;">**Pylenium**</mark> - an instance of Pylenium driver that interacts with the web

## pyc\_config

When using <mark style="color:yellow;">**`pyc`**</mark>, an instance of <mark style="color:orange;">**PyleniumConfig**</mark> is also created and can be managed per test class. You can access <mark style="color:yellow;">**`pyc_config`**</mark> as a fixture or directly from <mark style="color:yellow;">**`pyc.config`**</mark>

### Access by Fixture

```python
from pylenium.driver import Pylenium
from pylenium.config import PyleniumConfig

class TestSauceDemo:
    def test_land_on_products_page_after_login(self, pyc: Pylenium, pyc_config: PyleniumConfig):
        pyc_config.custom["user"] = "standard_user" # Set a value in one test...
        
        pyc.visit("https://www.saucedemo.com/")
        pyc.get("#user-name").type("standard_user")
        pyc.get("#password").type("secret_sauce")
        pyc.get("#login-button").click()
        assert pyc.contains("Products").should().be_visible()
        
    def test_add_item_to_cart_increments_counter_by_1(self, pyc: Pylenium, pyc_config: PyleniumConfig):
        print(pyc_config.custom.get("user")) # And use it in another test
        pyc.get("[id*='add-to-cart']").click()
        assert pyc.get("a.shopping_cart_link").should().have_text("1")
```

### Access Directly (recommended)

Recommended because it's fewer lines of code and you already have access via <mark style="color:orange;">**`Pylenium`**</mark>

```python
from pylenium.driver import Pylenium

class TestSauceDemo:
    def test_land_on_products_page_after_login(self, pyc: Pylenium):
        pyc.config.custom["user"] = "standard_user" # Set a value in one test...
        
        pyc.visit("https://www.saucedemo.com/")
        pyc.get("#user-name").type("standard_user")
        pyc.get("#password").type("secret_sauce")
        pyc.get("#login-button").click()
        assert pyc.contains("Products").should().be_visible()
        
    def test_add_item_to_cart_increments_counter_by_1(self, pyc: Pylenium):
        print(pyc.config.custom.get("user")) # And use it in another test
        pyc.get("[id*='add-to-cart']").click()
        assert pyc.get("a.shopping_cart_link").should().have_text("1")
```
