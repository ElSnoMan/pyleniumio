---
description: How to use Pylenium's logging
---

# Logging

Pylenium includes two custom <mark style="color:yellow;">**Log Levels**</mark> and a global <mark style="color:yellow;">**Logger**</mark> instance that you _can_ use.

## Log Levels

| Name     | Level | Note         |
| -------- | ----- | ------------ |
| CRITICAL | 50    |              |
| ERROR    | 40    |              |
| WARNING  | 30    |              |
| USER     | 25    | New          |
| INFO     | 20    |              |
| COMMAND  | 15    | New, Default |
| DEBUG    | 10    |              |

If you are familiar with logging, then the above table is straightforward. If not, then all you really need to know about these levels is that you can set the <mark style="color:yellow;">**Log Level**</mark> when executing tests, and any logs at the specified level or higher will be captured.

For example, if you wanted to set the <mark style="color:yellow;">**Log Level**</mark> to see only logs at **`INFO`** and higher, you would do this:

```bash
pytest --log-cli-level=INFO
```

{% hint style="info" %}
The above command would ignore logs _below_ the `INFO` level. In other words, ignore the **`COMMAND`** and **`DEBUG`** logs.
{% endhint %}

### &#x20;COMMAND Level

The **`COMMAND`** Log Level is used by <mark style="color:orange;">**Pylenium**</mark> for logging its commands in a cleaner and easier to parse format. You shouldn't use this level unless you _really want to_. Take a look at our <mark style="color:purple;">**`visit()`**</mark> command to see it in action:

```python
def visit(self, url: str) -> "Pylenium":
    log.command("py.visit() - Visit URL: `%s`", url)
    self.webdriver.get(url)
    return self
```

{% hint style="success" %}
Notice how the string uses the **`%s`** format and NOT the f-string format.

_**This is intentional!**_
{% endhint %}

### USER Level

The **`USER`** Log Level is meant for you! This is a convenient way for logging things if you don't want everything from the **`INFO`** level.

{% hint style="info" %}
I highly recommend creating your own loggers, but sometimes something simple like this is all you need 😄
{% endhint %}

To take advantage of this level, use <mark style="color:purple;">**`log.this()`**</mark>:

```python
# You can import this in any file
from pylenium.log import logger as log

# Log this
def add_to_cart(item: str, quantity: int):
    log.this("Adding %s %s to my cart", quantity, item)
    ...

# Then call the function
add_to_cart("Charizard", 3)
>>> USER Adding 3 Charizard to my cart
```

You can also directly use <mark style="color:purple;">**`py.log`**</mark>:

```python
# Log this
def add_to_cart(py: Pylenium, item: str, quantity: int):
    py.log.this("Adding %s %s to my cart", quantity, item)
    ...

# Then call the function
add_to_cart(py, "Charizard", 3)
>>> USER Adding 3 Charizard to my cart
```
