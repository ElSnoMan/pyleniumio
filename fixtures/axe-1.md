---
description: The main Pylenium fixture
---

# ✅ py

## Usage

The <mark style="color:yellow;">**`py`**</mark> fixture is the recommended way to use Pylenium because it gives each test its own instance of Pylenium which makes it easy to scale and parallelize.

```python
from pylenium.driver import Pylenium

def test_element_should_be_visible(py: Pylenium):
    py.visit("https://demoqa.com/buttons")
    assert py.contains("Click Me").should().be_visible()
```

{% hint style="success" %}
Import <mark style="color:yellow;">**`Pylenium`**</mark> and add the _**type hint**_ to your test (as shown above) so you get intellisense and autocomplete when writing tests :muscle:
{% endhint %}

## Arguments

* <mark style="color:yellow;">**`none`**</mark>

## Yields

* <mark style="color:orange;">**Pylenium**</mark> - an instance of Pylenium driver that interacts with the web

## py\_config

When using <mark style="color:yellow;">**`py`**</mark>, an instance of <mark style="color:orange;">**PyleniumConfig**</mark> is also created and can be managed per test. You can access <mark style="color:yellow;">**`py_config`**</mark> as a fixture or directly from <mark style="color:yellow;">**`py.config`**</mark>

### Access by Fixture

```python
from pylenium.driver import Pylenium
from pylenium.config import PyleniumConfig

def test_element_should_be_visible(py: Pylenium, py_config: PyleniumConfig):
    # Only this test will be against firefox
    py_config.driver.browser = "firefox"
    py.visit("https://demoqa.com/buttons")
    assert py.contains("Click Me").should().be_visible()
```

### Access Directly (recommended)

Recommended because it's fewer lines of code and you already have access via <mark style="color:orange;">**`Pylenium`**</mark>

```python
from pylenium.driver import Pylenium

def test_element_should_be_visible(py: Pylenium):
    # Only this test will be against firefox
    py.config.driver.browser = "firefox"
    py.visit("https://demoqa.com/buttons")
    assert py.contains("Click Me").should().be_visible()
```
