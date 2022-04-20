---
description: Pylenium provides fluent syntax to check for expected conditions.
---

# Should / Expected Conditions

Pylenium's [_<mark style="color:orange;">**Driver**</mark>_](../driver-commands/should.md), [_<mark style="color:orange;">**Element**</mark>_](../element-commands/should.md), and [_<mark style="color:orange;">**Elements**</mark>_](../elements-commands/elements.should.md) objects each have a `Should` API that allows you to write fluent-like code to wait and check for any expected conditions.

For example, to check that an element is visible on the webpage, you would do this:

{% code title="Pylenium" %}
```python
def test_element_is_visible(py):
    py.visit('https://qap.dev')
    assert py.get('a[href="/about"]').should().be_visible()
```
{% endcode %}

With Selenium, you normally use the `ExpectedConditions` class:

{% code title="Selenium" %}
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_element_is_visible():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, timeout=10)
    
    driver.get('https://qap.dev')
    element = wait.until(EC.visibility_of_element_located(By.CSS_SELECTOR, 'a[href="/about"]'))
    assert element.is_displayed()
```
{% endcode %}

### Similar Pages

* _<mark style="color:orange;">****</mark>_[_<mark style="color:orange;">**Driver.should()**</mark>_](../driver-commands/should.md)_<mark style="color:orange;">****</mark>_
* _****_[_<mark style="color:orange;">**Element.should()**</mark>_](../element-commands/should.md)_<mark style="color:orange;">****</mark>_
* _****_[_<mark style="color:orange;">**Elements.should()**</mark>_](../elements-commands/elements.should.md)_<mark style="color:orange;">****</mark>_
