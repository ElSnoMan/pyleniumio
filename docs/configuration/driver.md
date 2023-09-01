---
description: Configure the driver via the pylenium.json or the CLI.
---

# 🚗 Driver

## The Driver Settings

Supported Drivers:

* **Chrome**
* **Edge**
* **Safari**
* **Firefox**
* **Internet Explorer**

&#x20;Let's take a look at the Driver Settings in <mark style="color:orange;">**pylenium.json**</mark>

{% code title="pylenium.json" %}
```javascript
"driver": {
    "browser": "chrome",
    "remote_url": "",
    "wait_time": 10,
    "page_load_wait_time": 0,
    "options": [],
    "capabilities": {},
    "experimental_options": null,
    "extension_paths": [],
    "webdriver_kwargs": {},
    "seleniumwire_enabled": false,
    "seleniumwire_options": {},
    "local_path": ""
}
```
{% endcode %}

Let's break each one of these down so you know what they are for and how you can configure them.

### browser

{% hint style="info" %}
Default is <mark style="color:yellow;">**`chrome`**</mark>
{% endhint %}

This is the browser name - <mark style="color:purple;">`"chrome"`</mark> or <mark style="color:purple;">`"firefox"`</mark> or <mark style="color:purple;">`"ie"`</mark> or <mark style="color:purple;">`"safari"`</mark> or <mark style="color:purple;">`"edge"`</mark>

{% code title="pylenium.json" %}
```javascript
"driver": {
    "browser": "firefox"
}
```
{% endcode %}

{% code title="Terminal" %}
```bash
pytest tests --browser=firefox
```
{% endcode %}

### remote\_url

{% hint style="info" %}
Default is empty or**`""`**
{% endhint %}

This is used to connect to things like <mark style="color:yellow;">**Selenium Grid**</mark>**.**

{% hint style="success" %}
Check out [Run Tests in Containers](../guides/run-tests-in-containers.md) for an example of how to do this locally with <mark style="color:yellow;">**Docker**</mark>
{% endhint %}

{% code title="pylenium.json" %}
```javascript
"driver": {
    "remote_url": "http://localhost:4444/wd/hub"
}
```
{% endcode %}

{% code title="Terminal" %}
```bash
pytest tests --remote_url="http://localhost:4444/wd/hub"
```
{% endcode %}

### wait\_time

{% hint style="info" %}
Default is <mark style="color:yellow;">**`10`**</mark>
{% endhint %}

The global number of seconds for actions to wait for.

{% code title="pylenium.json" %}
```javascript
"driver": {
    "wait_time": 7
}
```
{% endcode %}

{% code title="Terminal" %}
```bash
You cannot set this from the command line
```
{% endcode %}

### page\_load\_wait\_time

{% hint style="info" %}
Default is <mark style="color:yellow;">**0**</mark>
{% endhint %}

The amount of time to wait for the page to load before raising an error.

```bash
# set it globally in CLI
--page_load_wait_time 10
```

```javascript
// set it globally in pylenium.json
{
    "driver": {
        "page_load_wait_time": 10
    }
}
```

```python
# override the global page_load_wait_time just for the current test
py.set_page_load_timeout(10)
```

### options

{% hint style="info" %}
Default is empty or **`[]`**
{% endhint %}

A list of browser options to include when instantiating Pylenium.

{% code title="pylenium.json" %}
```javascript
"driver": {
    "options": ["headless", "incognito"]
}
```
{% endcode %}

{% code title="Terminal" %}
```bash
pytest tests --options="headless, incognito"
```
{% endcode %}

### experimental\_options

{% hint style="info" %}
Default is <mark style="color:yellow;">**`null`**</mark> or <mark style="color:yellow;">**`None`**</mark>
{% endhint %}

A list of experimental options to include in the driver. These can only be added using <mark style="color:orange;">**pylenium.json**</mark>

```javascript
{
    "experimental_options": [
        {"useAutomationExtension": false},
        {"otherName": "value"}
    ]
}
```

### capabilities

{% hint style="info" %}
Default is empty or `{}`
{% endhint %}

A dictionary of the desired capabilities to include when instantiating Pylenium.

{% code title="pylenium.json" %}
```python
{
    "driver": {
        "capabilities": {
            "enableVNC": true,
            "enableVideo": false,
            "name": "value"
        }
    }
}
```
{% endcode %}

{% code title="Terminal" %}
```python
pytest tests --caps = '{"name": "value", "boolean": true}'
```
{% endcode %}

### extension\_paths

The list of extensions to be included when instantiating Pylenium.

{% hint style="info" %}
Default is empty or `[]`
{% endhint %}

```javascript
{
    "driver": {
        "extension_paths": ["path_to_crx.crx", "other-path.crx"]
    }
}
```

### seleniumwire\_enabled

{% hint style="info" %}
Default is <mark style="color:yellow;">**false**</mark>
{% endhint %}

Use a SeleniumWire-enabled Chrome or Firefox driver.

{% code title="pylenium.json" %}
```javascript
"driver": {
    "seleniumwire_enabled": false
}
```
{% endcode %}

{% code title="Terminal" %}
```bash
pytest --seleniumwire_enabled=true
```
{% endcode %}

### seleniumwire\_options

{% hint style="info" %}
Default is <mark style="color:yellow;">**{}**</mark>
{% endhint %}

Options for the SeleniumWire-enabled Chrome or Firefox driver.

{% code title="pylenium.json" %}
```javascript
"driver": {
    "seleniumwire_options": {}
}
```
{% endcode %}

{% hint style="success" %}
See their docs on [how to use it](https://www.zenrows.com/blog/selenium-wire#chromium-options) and the options you can set
{% endhint %}
