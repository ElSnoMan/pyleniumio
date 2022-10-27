---
description: >-
  pytest is a modern and powerful Test Framework and we want to get intellisense
  and autocomplete
---

# 2. Setup pytest

## 1. Install pyleniumio

Install **Pylenium** into your [Virtual Environment](virtual-environments.md) if you haven't already:

{% tabs %}
{% tab title="pip" %}
{% code title="Terminal $ (venv)" %}
```bash
pip install pyleniumio
```
{% endcode %}
{% endtab %}

{% tab title="poetry" %}
poetry add pyleniumio
{% endtab %}

{% tab title="pipenv" %}
{% code title="Terminal $ (venv)" %}
```
pipenv install pyleniumio
```
{% endcode %}
{% endtab %}
{% endtabs %}

## 2. Initialize Pylenium

{% code title="Terminal $ (venv)" %}
```
pylenium init
```
{% endcode %}

{% hint style="success" %}
Execute this command at your Project Root
{% endhint %}

This creates three files:

* `conftest.py` - This has the fixtures needed for Pylenium.
* `pylenium.json` - This is the [configuration ](../configuration/pylenium.json.md)file for Pylenium.
* `pytest.ini` - This is the configuration file for pytest and is used to connect to [ReportPortal](../cli/report-portal.md)

By default, Pylenium uses the Chrome browser. Chrome must be installed on the machine, but you don't have to worry about installing any of the drivers.

## 3. Select pytest as the Test Framework

To get the most out of your IDE, you need to configure it to use **pytest** as the Test Framework. This will give you:

* Intellisense
* Autocomplete
* Run/Debug Test functionality with breakpoints
* more depending on IDE

{% tabs %}
{% tab title="VS Code" %}
```
Open Command Palette (CMD + SHIFT + P or CTRL + SHIFT + P)
Search for "Python: Configure Tests"
Select pytest
```
{% endtab %}

{% tab title="PyCharm" %}
{% code title="(RECOMMENDED IDE)" %}
```
Open Preferences (or Settings)
Open Tools > Python Integrated Tools
Select pytest in the "Default test runner" dropdown
```
{% endcode %}
{% endtab %}
{% endtabs %}

{% hint style="info" %}
Visit the pytest docs for more info on how to use it: [https://docs.pytest.org/](https://docs.pytest.org/)
{% endhint %}
