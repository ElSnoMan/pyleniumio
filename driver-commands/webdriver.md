---
description: The property to get the current instance of Selenium's WebDriver.
---

# webdriver

## Syntax

```
py.webdriver -> WebDriver
```

## Usage

{% code title="correct usage" %}
```python
py.webdriver
```
{% endcode %}

{% code title="incorrect usage" %}
```python
py.webdriver()
```
{% endcode %}

## Arguments

* None

## Yields

* <mark style="color:orange;">**WebDriver**</mark>  - The current instance of Selenium WebDriver that Pylenium is wrapping

## Examples

Most scenarios won't need this, but it's provided just in case. The biggest reasons to use <mark style="color:purple;">`py.webdriver`</mark>

* access functionality that may not exist in Pylenium
* functionality that requires you pass in a WebDriver

```python
# get WebDriver's current Capabilities
caps = py.webdriver.capabilities
```

```python
# function requires a WebDriver
actions = ActionChains(py.webdriver)
```

