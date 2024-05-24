---
description: The configuration file for Pylenium
---

# 📄 pylenium.json

## Configure with a JSON File

If you don't want to use Pylenium's defaults but you don't want to configure it via the CLI, you can create a <mark style="color:orange;">**pylenium.json**</mark> file at the <mark style="color:yellow;">**Project Root**</mark> (same directory as our <mark style="color:orange;">**conftest.py**</mark> file) and do it with a JSON instead.

{% hint style="info" %}
<mark style="color:orange;">**pylenium.json**</mark> is already created when using the <mark style="color:purple;">**`pylenium init`**</mark> command
{% endhint %}

Here are all of the current settings (and their defaults) you can configure right now:

```javascript
{
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
    "local_path": ""
  },
  "logging": {
    "screenshots_on": true
  },
  "viewport": {
    "maximize": true,
    "width": 1440,
    "height": 900,
    "orientation": "portrait"
  },

  "custom": {}
}

```

## Change a single value

{% hint style="info" %}
You only need to change the values you care about.
{% endhint %}

If I only wanted to change the browser to be `"firefox"`, then only include that:

```bash
{
  "driver": {
    "browser": "firefox"
  }
}
```

## Adding custom values

{% hint style="info" %}
You can add any objects within the <mark style="color:yellow;">**custom**</mark> object to be used by <mark style="color:orange;">**py.config**</mark>
{% endhint %}

Adding your own key/value pairs is easy:

```bash
{
  "custom": {
    "env_url": "https://staging.our-app.com"
  }
}
```

Now you can use it like any other dictionary in Python:

```python
py.config.custom.get("env_url")

---or---

py.config.custom["env_url"]
```

### Complex custom objects

More complex or nested objects are easy to add as well:

```bash
{
  "custom": {
    "environment": {
      "url": "https://staging.our-app.com",
      "username": "foo",
      "password": "bar",
      "clusters": [ "cl01", "cl03", "cl05" ]
    }
  }
}
```

It's still just a Python dictionary, so you can easily access them:

```python
# Get the entire environment object
py.config.custom.get("environment")

# Get only the url
py.config.custom["environment"]["url"]

# Get the first item in the list of clusters
py.config.custom["environment"]["clusters"][0]
```

## Multiple Versions

You can have multiple <mark style="color:yellow;">**`pylenium.json`**</mark> files and pick which one to use when executing tests.

For example, you can have multiple at your Project Root:

```
📂 Project
    📃 conftest.py
    📃 pylenium.json
    📃 local.pylenium.json
    ...
```

or store them in another folder:

```
📂 Project
    📃 conftest.py
    📃 pylenium.json
    📂 config
	📃 local.pylenium.json
	📃 dev.pylenium.json
	📃 stage.config.json
```

{% hint style="success" %}
Keep the original `pylenium.json` at the Project Root so the default behavior continues to work 😉
{% endhint %}



Then, use the <mark style="color:yellow;">**`--pylenium_json`**</mark> argument to pick which to use:

```bash
pytest --pylenium_json="local.pylenium.json"

pytest --pylenium_json="config/dev.pylenium.json"
```

{% hint style="info" %}
You can name your custom Pylenium config files whatever you like, but they MUST be `.json` and have the same shape (aka schema) as the default `pylenium.json`
{% endhint %}

