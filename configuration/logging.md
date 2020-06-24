---
description: Configure logging via the pylenium.json or the CLI.
---

# Logging

## Levels

Pylenium has 3 logging levels:

* `'off'`
* `'info' (default)`
* `'debug'`

When you start a Test Run, Pylenium will create a **test\_results** directory at your Project Root.

{% hint style="info" %}
You should put **test\_results** in your .`gitignore`
{% endhint %}

By default, each test using the `py` fixture will have its own subdirectory with a `test_log.txt` and, if the test fails, a screenshot.

You can easily control the logging and screenshots by setting the values in `pylenium.json` or passing in command-line arguments.

### off

Like the name suggests, this will turn off all `INFO` and higher entries, which is almost everything.

{% hint style="info" %}
You will still get a `test_log.txt` file, but it will only have basic info of the test like chromedriver version.
{% endhint %}

{% code title="pylenium.json" %}
```text
"pylog_level": "off"
```
{% endcode %}

{% code title="Terminal" %}
```text
python -m pytest tests --pylog_level=off
```
{% endcode %}

### info

This will include basic info as well as the `INFO` , `ACTION`, `STEP` entries.

{% hint style="success" %}
This is the **default** configuration, so you don't need to explicitly set these.
{% endhint %}

{% code title="pylenium.json" %}
```text
"pylog_level": "info"
```
{% endcode %}

{% code title="Terminal" %}
```text
python -m pytest tests --pylog_level=info
```
{% endcode %}

### debug

This will include everything in **info** as well as the `DEBUG` , `WARNING`, `ERROR` and `FATAL` entries.

{% hint style="info" %}
You can use `py.log.debug(message)` to log debugging entries!
{% endhint %}

{% code title="pylenium.json" %}
```text
"pylog_level": "debug"
```
{% endcode %}

{% code title="Terminal" %}
```text
python -m pytest tests --pylog_level=debug
```
{% endcode %}

## Screenshots

By default, if a test fails, Pylenium will take a screenshot and include it in the respective `test_results` test directory.

This can easily be turned **off.**

{% code title="pylenium.json" %}
```text
"screenshots_on": False
```
{% endcode %}

{% code title="Terminal" %}
```text
python -m pytest tests --screenshots_on=false
```
{% endcode %}

