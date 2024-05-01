---
description: The command to execute a method or function as a condition to wait for.
---

# wait

{% hint style="success" %}
Pylenium provides a <mark style="color:orange;">**Should API**</mark> for [Driver](should.md), [Element](../element-commands/should.md), and [Elements](../elements-commands/elements.should.md) objects. This is the **recommended** way to wait for things in Pylenium.

However, you can use Selenium's ExpectedConditions class or lambdas as shown on the rest of this page.
{% endhint %}



There are two types of Wait objects:

* **WebDriverWait (default)**
  * Directly from Selenium
  * Returns <mark style="color:orange;">**`WebElement`**</mark> and <mark style="color:orange;">**`List[WebElement]`**</mark>
* **PyleniumWait**
  * Returns <mark style="color:orange;">**`Element`**</mark> and <mark style="color:orange;">**`Elements`**</mark>
  * Has a built-in <mark style="color:purple;">`.sleep()`</mark> method

<mark style="color:purple;">`wait.until(condition)`</mark> is the most common use of Wait and allows you to wait until the condition returns a _non-False_ value.

However, both Waits require the condition to use a WebDriver. In the example below, we can pass in a **lambda** (aka anonymous function) where `x` _is_ the **WebDriver**.

```python
# .is_displayed() returns a bool, so the return value is True
py.wait().until(lambda x: x.find_element(By.ID, "foo").is_displayed())
```

```python
# the WebElement is returned once the element is found in the DOM
py.wait().until(lambda x: x.find_element(By.ID, "foo"))
```

```python
# because use_py=True, this will now return Element instead
# also, this will wait up to 5 seconds instead of the default in pylenium.json
py.wait(5, use_py=True).until(lambda x: x.find_element(By.ID, "foo"))
```

## Syntax

```python
# all 3 parameters are Optional with defaults
py.wait(timeout=0, use_pylenium=False, ignored_exceptions: list = None)
```

## Usage

The usages are almost identical between the Wait objects, but you need to identify why you need to use a Wait in the first place. Pylenium does a lot of waiting for you automatically, but not for everything.

{% hint style="info" %}
Remember, the biggest difference is what is returned: **`WebElement`** vs **`Element`**
{% endhint %}

{% hint style="success" %}
Good framework and test design includes waiting for the right things. This is called **Synchronization**
{% endhint %}

### WebDriverWait

This is the default Wait object. This will return <mark style="color:orange;">**WebElement**</mark>, so you won't have Pylenium's Element commands like <mark style="color:purple;">`.hover()`</mark> - that is what <mark style="color:orange;">**PyleniumWait**</mark> is for.

* Using the defaults

{% code title="defaults" %}
```python
# uses WebDriverWait and returns WebElement once '#save' is found
py.wait().until(lambda x: x.find_element(By.ID, "save")).click()
```
{% endcode %}

* Using custom <mark style="color:orange;">**`timeout`**</mark>

{% code title="Custom timeout" %}
```python
# uses WebDriverWait but overrides the default wait_time used in pylenium.json
py.wait(5).until(lambda x: x.find_element(By.ID, "login-button").is_enabled())
```
{% endcode %}

* Using <mark style="color:orange;">**`ignored_exceptions`**</mark>

By default, the only exception that is ignored is the <mark style="color:purple;">`NoSuchElementException`</mark>. You can change this by adding a list of Exceptions that you want your condition to ignore.

{% code title="ignored_exceptions" %}
```python
# ignore exceptions every time the condition is executed
# also, this will return True because
    # x.title == 'QA at the Point'
# is a boolean expression
exceptions = [NoSuchElementException, WebDriverException]
py.wait(ignored_exceptions=exceptions).until(lambda x: x.title == "Pylenium.io")
```
{% endcode %}

* Combine arguments

```python
exceptions = [NoSuchElementException, WebDriverException]
py.wait(7, ignored_exceptions=exceptions).until(lambda x: x.execute_script("js'")
```

### PyleniumWait

If you want to return Pylenium objects like <mark style="color:orange;">**`Element`**</mark> and <mark style="color:orange;">**`Elements`**</mark>, then set <mark style="color:purple;">`use_py=True`</mark>`.` Otherwise, it works the same way as WebDriverWait.

{% code title="PyleniumWait with default timeout" %}
```python
py.wait(use_py=True).until(lambda x: x.find_element(By.ID, "menu")).hover()
```
{% endcode %}

{% code title="PyleniumWait with custom timeout" %}
```python
py.wait(5, use_py=True).until(lambda x: x.find_element(By.ID, "menu")).hover()
```
{% endcode %}

* <mark style="color:orange;">**PyleniumWait**</mark> also includes a <mark style="color:purple;">**`.sleep()`**</mark> command

```python
# time.sleep() for 3 seconds
py.wait(use_py=True).sleep(3)
```

### Expected Conditions

Expected Conditions are a list of pre-built conditions that you can use in your Waits and can be used in either WebDriverWait or PyleniumWait to replace the lambda functions in the examples above.

```python
from selenium.webdriver.support import expected_conditions as EC

py.wait().until(EC.title_is("Pylenium.io"))
```

## Yields

* <mark style="color:orange;">**Any**</mark> - Whatever the non-False value of the condition is

## Raises

* <mark style="color:orange;">**`TimeoutException`**</mark> if the condition is not met within the timeout time
* Depending on the condition, it would raise other Exceptions. If you know which ones are expected, you can include them in the <mark style="color:purple;">**`ignored_exceptions`**</mark> as an argument.
