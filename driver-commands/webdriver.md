---
description: The property to get the current instance of Selenium's WebDriver.
---

# webdriver

## Syntax

```
py.webdriver
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

* **(WebDriver)** The current instance of WebDriver that Pylenium is wrapping

## Examples

Most scenarios won't need this, but it's provided just in case. The biggest reasons to use `py.webdriver`

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

