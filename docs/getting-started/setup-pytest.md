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
{% code title="Terminal" %}
```bash
poetry add pyleniumio
```
{% endcode %}
{% endtab %}

{% tab title="pipenv" %}
{% code title="Terminal " %}
```bash
pipenv install pyleniumio
```
{% endcode %}
{% endtab %}
{% endtabs %}

{% hint style="success" %}
`poetry` and `pipenv` auto-generate virtual environments for you!
{% endhint %}

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

* <mark style="color:yellow;">**`conftest.py`**</mark> - This has the fixtures needed for Pylenium
* <mark style="color:yellow;">**`pylenium.json`**</mark> - This is the [configuration ](../configuration/pylenium.json.md)file for Pylenium
* <mark style="color:yellow;">**`pytest.ini`**</mark> - This is the configuration file for pytest

By default, Pylenium uses the Chrome browser. Chrome must be installed on the machine, but you don't have to worry about installing any of the drivers.

## 3. Select pytest as the Test Framework

To get the most out of your IDE, you need to configure it to use <mark style="color:yellow;">**pytest**</mark> as the Test Framework. This will give you:

* Intellisense
* Autocomplete
* Run/Debug Test functionality with breakpoints
* more depending on IDE

{% tabs %}
{% tab title="VS Code" %}
```
1. Open Command Palette (CMD + SHIFT + P or CTRL + SHIFT + P)
2. Search for "Python: Configure Tests"
3. Select pytest
```
{% endtab %}

{% tab title="PyCharm" %}
```
1. Open Preferences (or Settings)
2. Open Tools > Python Integrated Tools
3. Select pytest in the "Default test runner" dropdown
```
{% endtab %}
{% endtabs %}

{% hint style="info" %}
Visit the pytest docs for more info on how to use it: [https://docs.pytest.org/](https://docs.pytest.org/)
{% endhint %}
