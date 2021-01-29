---
description: Configure the driver via the pylenium.json or the CLI.
---

# Driver

## The Driver Settings

Supported Drivers:

* **Chrome**
* **Firefox**
* **IE**
* **Opera**
* **Edge \(Chromium\)**

 Let's take a look at the Driver Settings in `pylenium.json`

{% code title="pylenium.json" %}
```javascript
"driver": {
    "browser": "chrome",
    "remote_url": "",
    "wait_time": 10,
    "page_load_wait_time": 0,
    "options": [],
    "experimental_options": null,
    "capabilities": {},
    "extension_paths": [],
    "version": "latest"
  }
```
{% endcode %}

Let's break each one of these down so you know what they are for and how you can configure them.

### browser

{% hint style="info" %}
Default is **`"chrome"`**
{% endhint %}

This is the browser name - `"chrome"` or `"firefox"` or `"ie"` or `"opera"` or `"edge"`

{% code title="pylenium.json" %}
```javascript
"driver": {
    "browser": "firefox"
}
```
{% endcode %}

{% code title="Terminal" %}
```bash
python -m pytest tests --browser=firefox
```
{% endcode %}

### remote\_url

{% hint style="info" %}
Default is empty or**`""`**
{% endhint %}

This is used to connect to things like **Selenium Grid.**

{% hint style="success" %}
Check out [Run Tests in Containers](../guides/run-tests-in-containers.md) for an example of how to do this locally with **Docker**
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
python -m pytest tests --remote_url="http://localhost:4444/wd/hub"
```
{% endcode %}

### wait\_time

{% hint style="info" %}
Default is **`10`**
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
Default is 0
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
python -m pytest tests --options="headless, incognito"
```
{% endcode %}

### experimental\_options

{% hint style="info" %}
Default is `null` or `None`
{% endhint %}

A list of experimental options to include in the driver. These can only be added using `pylenium.json`

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
--caps = '{"name": "value", "boolean": true}'
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

### version

{% hint style="info" %}
Default is **`"latest"`**
{% endhint %}

The browser version to use.

{% code title="pylenium.json" %}
```javascript
"driver": {
    "version": "latest"
}
```
{% endcode %}

{% code title="Terminal" %}
```bash
You cannot set the browser version this way
```
{% endcode %}

