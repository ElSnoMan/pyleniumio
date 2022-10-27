---
description: Pylenium has commands for working with allure reporting
---

# Allure CLI

These are "convenience" commands if you are new to allure, but you can use these Pylenium commands or use the <mark style="color:yellow;">**`allure`**</mark>  CLI directly _(recommended)_

## allure install

Install the <mark style="color:yellow;">**`allure`**</mark> CLI on the current machine.

{% code title="Terminal" %}
```bash
pylenium allure install
```
{% endcode %}

Pylenium detects your operating system and _tries_ to install allure with the appropriate installation commands. However, it's recommended that you use their official installation docs instead.

{% hint style="warning" %}
[https://docs.qameta.io/allure-report/#\_installing\_a\_commandline](https://docs.qameta.io/allure-report/#\_installing\_a\_commandline)
{% endhint %}

## allure check

Check that there is valid allure CLI installed on the current machine.

{% code title="Terminal" %}
```bash
pylenium allure check
```
{% endcode %}

* If successful, a message is displayed with the current version of allure
* Otherwise, allure is not installed or not added to the PATH correctly

{% hint style="info" %}
This is equivalent to the following allure command ⬇️
{% endhint %}

{% code title="Terminal" %}
```bash
allure --version
```
{% endcode %}

## allure serve

Starts the allure server, generates the report, and serves it as a new browser tab.

{% code title="Terminal" %}
```bash
pylenium allure serve --folder [FOLDER]
```
{% endcode %}

{% hint style="info" %}
This is equivalent to the following allure command ⬇️
{% endhint %}

{% code title="Terminal" %}
```bash
allure serve [FOLDER]
```
{% endcode %}

### Example

Run your tests with pytest and specify that the output be saved to the **`allure-report`** folder

{% code title="Terminal" %}
```bash
pytest --alluredir=allure-report
```
{% endcode %}

With the test run finished we can serve the report and see the results

{% code title="Terminal" %}
```bash
pylenium allure serve --folder allure-report
```
{% endcode %}
