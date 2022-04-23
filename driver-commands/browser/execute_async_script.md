---
description: The command to execute async javascript into the browser.
---

# execute\_async\_script

Similar to the [execute\_script](execute\_script.md) command, you can pass in any <mark style="color:purple;">javascript string</mark> and <mark style="color:purple;">\*args</mark>. The main difference is that you can execute _<mark style="color:yellow;">**asynchronous**</mark>_ javascript. For example, using **callbacks**.

```python
script = "var callback = arguments[arguments.length - 1]; " \
         "window.setTimeout(function(){ callback('timeout') }, 3000);"
driver.execute_async_script(script)
```

## Syntax

```python
py.execute_async_script(javascript: str) -> Any
py.execute_async_script(javascript: str, *args) -> Any
```

## Usage

{% code title="correct usage" %}
```python
# Yields the value of document.title
py.execute_async_script("return document.title;")

---or---

# Yields the .innerText of the element with the id of 'foo'
py.execute_async_script("return document.getElementById(arguments[0]).innerText", "foo")
```
{% endcode %}

{% code title="incorrect usage" %}
```python
# Errors, 'execute_script' yields a WebElement, not a Pylenium Element
py.execute_async_script("return document.getElementById(arguments[0])").get()
```
{% endcode %}

## Arguments

* <mark style="color:purple;">`javascript (str)`</mark> - The async javascript to execute
* <mark style="color:purple;">`*args (Any)`</mark> - A comma-separated list of arguments to pass into the javascript string

{% hint style="info" %}
You can access the **\*args** in the javascript by using `arguments[0]`, `arguments[1]`, etc.
{% endhint %}

## Yields

* <mark style="color:orange;">**Any**</mark> - This will return whatever is in the `return statement` of your javascript.

{% hint style="info" %}
If you do not include a **return**, then `.execute_async_script()` will return **None**
{% endhint %}

## Examples

```python
# You can pass in complex objects
ul_element = py.get("ul")
py.execute_script("return arguments[0].children;", ul_element.webelement)
# We use the .webelement property to send Selenium's WebElement
# that is understood by the browser
```

```python
# You can create complex javascript strings
get_siblings_script = '''
    elem = document.getElementById(arguments[0]);
    var siblings = [];
    var sibling = elem.parentNode.firstChild;

    while (sibling) {
        if (sibling.nodeType === 1 && sibling !== elem) {
            siblings.push(sibling);
        }
        sibling = sibling.nextSibling
    }
    return siblings;
    '''
siblings = self.py.execute_async_script(get_siblings_script, "foo")
```
