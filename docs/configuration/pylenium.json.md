---
description: The configuration file for Pylenium
---

# pylenium.json

## Configure with a JSON File

If you don't want to use Pylenium's defaults but you don't want to configure it via the CLI, you can create a **`pylenium.json`** file at the Project Root \(same directory as our `conftest.py` file\) and do it with a JSON instead.

Here are all of the current settings \(and their defaults\) you can configure right now:

```javascript
{
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
  },

  "logging": {
    "screenshots_on": true,
    "pylog_level": "info"
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
You can add any objects within the **`custom`** object to be used by **`py.config`**
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
py.config.custom.get('env_url')

---or---

py.config.custom['env_url']
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
py.config.custom.get('environment')

# Get only the url
py.config.custom['environment']['url']

# Get the first item in the list of clusters
py.config.custom['environment']['clusters'][0]
```
