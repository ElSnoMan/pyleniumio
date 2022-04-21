---
description: The CLI comes with commands to initialize and create Pylenium files, and more.
---

# Pylenium CLI

## pylenium init

Initializes Pylenium into the current directory. This creates Pylenium's required files:

* `conftest.py`
* `pylenium.json`
* `pytest.ini`

{% code title="Terminal $" %}
```bash
pylenium init
```
{% endcode %}

{% hint style="success" %}
Make sure to run this command at the <mark style="color:yellow;">**Project Root**</mark> (aka Workspace)
{% endhint %}

{% hint style="info" %}
By default, this will not overwrite Pylenium files if they already exist.
{% endhint %}

## Overwrite conftest.py file

You can overwrite an existing <mark style="color:orange;">**conftest.py**</mark> file with the latest version by using the `-c` flag.

{% code title="Terminal $" %}
```bash
pylenium init -c
```
{% endcode %}

## Overwrite pylenium.json file

You can overwrite an existing <mark style="color:orange;">**pylenium.json**</mark> file with the latest defaults by using the `-p` flag.

{% code title="Terminal $" %}
```bash
pylenium init -p
```
{% endcode %}

## Overwrite pytest.ini file

You can overwrite an existing <mark style="color:orange;">**pytest.ini**</mark> file with the latest defaults by using the `-i` flag.\\

{% code title="Terminal $" %}
```bash
pylenium init -i
```
{% endcode %}
