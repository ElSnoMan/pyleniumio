---
description: A single instance of Pylenium for an entire Test Session
---

# ❌ pys

## Usage

The <mark style="color:yellow;">**`pys`**</mark> fixture is used if you want a single instance of Pylenium that is _<mark style="color:red;">**shared across all tests**</mark>_ within a Test Session.

{% hint style="danger" %}
Using [**py**](axe-1.md) is the recommended way of working with Pylenium. Sharing data and states across tests is a _<mark style="color:red;">**bad practice**</mark>_. For example, _you cannot run tests in parallel in this mode_.
{% endhint %}

```python
from pylenium.driver import Pylenium

class TestSauceDemo:
    def test_land_on_products_page_after_login(self, pys: Pylenium):
        pys.visit("https://www.saucedemo.com/")
        pys.get("#user-name").type("standard_user")
        pys.get("#password").type("secret_sauce")
        pys.get("#login-button").click()
        assert pys.contains("Products").should().be_visible()
        
    def test_add_item_to_cart_increments_counter_by_1(self, pys: Pylenium):
        pys.get("[id*='add-to-cart']").click()
        assert pys.get("a.shopping_cart_link").should().have_text("1")
```

{% hint style="success" %}
Import <mark style="color:yellow;">**`Pylenium`**</mark> and add the _**type hint**_ to your tests (as shown above) so you get intellisense and autocomplete when writing tests :muscle:
{% endhint %}

## Arguments

* <mark style="color:yellow;">**`none`**</mark>

## Yields

* <mark style="color:orange;">**Pylenium**</mark> - an instance of Pylenium driver that interacts with the web

## pys\_config

When using <mark style="color:yellow;">**`pys`**</mark>, an instance of <mark style="color:orange;">**PyleniumConfig**</mark> is also created and can be managed for the test session. You can access <mark style="color:yellow;">**`pys_config`**</mark> as a fixture or directly from <mark style="color:yellow;">**`pys.config`**</mark>

### Access by Fixture

```python
from pylenium.driver import Pylenium
from pylenium.config import PyleniumConfig

class TestSauceDemo:
    def test_land_on_products_page_after_login(self, pys: Pylenium, pys_config: PyleniumConfig):
        pys_config.custom["user"] = "standard_user" # Set a value in one test...
        
        pys.visit("https://www.saucedemo.com/")
        pys.get("#user-name").type("standard_user")
        pys.get("#password").type("secret_sauce")
        pys.get("#login-button").click()
        assert pys.contains("Products").should().be_visible()
        
    def test_add_item_to_cart_increments_counter_by_1(self, pys: Pylenium, pys_config: PyleniumConfig):
        print(pys_config.custom.get("user")) # And use it in another test
        pys.get("[id*='add-to-cart']").click()
        assert pys.get("a.shopping_cart_link").should().have_text("1")
```

### Access Directly (recommended)

Recommended because it's fewer lines of code and you already have access via <mark style="color:orange;">**`Pylenium`**</mark>

```python
from pylenium.driver import Pylenium

class TestSauceDemo:
    def test_land_on_products_page_after_login(self, pys: Pylenium):
        pys.config.custom["user"] = "standard_user" # Set a value in one test...
        
        pys.visit("https://www.saucedemo.com/")
        pys.get("#user-name").type("standard_user")
        pys.get("#password").type("secret_sauce")
        pys.get("#login-button").click()
        assert pys.contains("Products").should().be_visible()
        
    def test_add_item_to_cart_increments_counter_by_1(self, pys: Pylenium):
        print(pys.config.custom.get("user")) # And use it in another test
        pys.get("[id*='add-to-cart']").click()
        assert pys.get("a.shopping_cart_link").should().have_text("1")
```
