---
description: The command to execute javascript into the browser.
---

# execute\_script

## Syntax

```python
py.execute_script(javascript)
py.execute_script(javascript, *args)
```

## Usage

{% code title="correct usage" %}
```python
# Yields the value of document.title
py.execute_script('return document.title;')

---or---

# Yields the .innerText of the element with the id of 'foo'
py.execute_script('return document.getElementById(arguments[0]).innerText', 'foo')
```
{% endcode %}

{% code title="incorrect usage" %}
```python
# Errors, 'execute_script' yields a WebElement, not a Pylenium Element
py.execute_script('return document.getElementById(arguments[0])').get()
```
{% endcode %}

## Arguments

* `javascript (str)` - The javascript to execute
* `*args (Any)` - A comma-separated list of arguments to pass into the javascript string

{% hint style="info" %}
You can access the **\*args** in the javascript by using `arguments[0]`, `arguments[1]`, etc.
{% endhint %}

## Yields

* **\(Any\)** This will return whatever is in the `return statement` of your javascript.

{% hint style="info" %}
If you do not include a **return**, then `.execute_script()` will return **None**
{% endhint %}

## Examples

```python
# You can pass in complex objects
ul_element = py.get('ul')
py.execute_script('return arguments[0].children;', ul_element.webelement)
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
siblings = self.py.execute_script(get_siblings_script, 'foo')
```

