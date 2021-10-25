---
description: The command to execute a method or function as a condition to wait for.
---

# wait

There are two types of Wait objects:

- **WebDriverWait \(default\)**
  - returns `WebElement` and `List[WebElement]`
- **PyleniumWait**
  - returns `Element` and `Elements`
  - has a built-in `.sleep()` method

`wait.until(condition)` is the most common use of Wait and allows you to wait until the condition returns a _non-False_ value.

However, both Waits require the condition to use a WebDriver. In the example below, we can pass in a **lambda** \(aka anonymous function\) where `x` _is_ the **WebDriver**.

```python
# .is_displayed() returns a bool, so the return value is True
py.wait().until(lambda x: x.find_element(By.ID, 'foo').is_displayed())
```

```python
# the WebElement is returned once the element is found in the DOM
py.wait().until(lambda x: x.find_element(By.ID, 'foo'))
```

```python
# because use_py=True, this will now return Element instead
# also, this will wait up to 5 seconds instead of the default in pylenium.json
py.wait(5, use_py=True).until(lambda x: x.find_element(By.ID, 'foo'))
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
Good framework and test design includes waiting for the right things.
{% endhint %}

### WebDriverWait

This is the default Wait object. This will return WebElement, so you won't have Pylenium's Element commands like `.hover()` - that is what PyleniumWait is for.

- Using the defaults

{% code title="defaults" %}

```python
# uses WebDriverWait and returns WebElement once '#save' is found
py.wait().until(lambda x: x.find_element(By.ID, 'save')).click()
```

{% endcode %}

- Using custom **`timeout`**

{% code title="WebDriverWait with custom timeout" %}

```python
# uses WebDriverWait but overrides the default wait_time used in pylenium.json
py.wait(5).until(lambda x: x.find_element(By.ID, 'login-button').is_enabled())
```

{% endcode %}

- Using **`ignored_exceptions`**

By default, the only exception that is ignored is the `NoSuchElementException`. You can change this by adding a list of Exceptions that you want your condition to ignore.

{% code title="WebDriverWait with ignored\_exceptions" %}

```python
# ignore exceptions every time the condition is executed
# also, this will return True because
    # x.title == 'QA at the Point'
# is a boolean expression
exceptions = [NoSuchElementException, WebDriverException]
py.wait(ignored_exceptions=exceptions).until(lambda x: x.title == 'Pylenium.io')
```

{% endcode %}

- Combine arguments

```python
exceptions = [NoSuchElementException, WebDriverException]
py.wait(7, ignored_exceptions=exceptions).until(lambda x: x.execute_script('js'))
```

### PyleniumWait

If you want to return Pylenium objects like `Element` and `Elements`, then set `use_py=True.` Otherwise, it works the same way as WebDriverWait.

{% code title="PyleniumWait with default timeout" %}

```python
py.wait(use_py=True).until(lambda x: x.find_element(By.ID, 'menu')).hover()
```

{% endcode %}

{% code title="PyleniumWait with custom timeout" %}

```python
py.wait(5, use_py=True).until(lambda x: x.find_element(By.ID, 'menu')).hover()
```

{% endcode %}

- PyleniumWait also includes a **`.sleep()`** command

```python
# time.sleep() for 3 seconds
py.wait(use_py=True).sleep(3)
```

### Expected Conditions

Expected Conditions are a list of pre-built conditions that you can use in your Waits and can be used in either WebDriverWait or PyleniumWait to replace the lambda functions in the examples above.

```python
from selenium.webdriver.support import expected_conditions as ec

py.wait().until(ec.title_is('Pylenium.io'))
```

{% hint style="info" %}
**`title_is()`** is just one of the many pre-built conditions in this module. Give it a try!
{% endhint %}

## Yields

- Whatever the non-False value of the condition is

## Raises

- **`TimeoutException`** if the condition is not met within the timeout time
- Depending on the condition, it would raise other Exceptions. If you know which ones are expected, you can include them in the **`ignored_exceptions`** as an argument.
