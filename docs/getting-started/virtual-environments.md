---
description: This is the first, critical piece to modern software development with Python.
---

# 1. Virtual Environments

## A Virtual Environment is required

**PyCharm** creates a venv by default when you create a new Project.

{% hint style="success" %}
You can skip this step if you already have a Virtual Environment in your Project
{% endhint %}

## What is a Virtual Environment?&#x20;

Without Virtual Environments (**venv**), everything you install would be global to your machine. Every project you have would be sharing the same packages and dependencies which could cause clashes or unwanted side effects.

Luckily, **venvs** are easy to setup. Open a Terminal in the context of your Project Directory.

{% hint style="warning" %}
We assume you already have **python3** installed on your machine
{% endhint %}

{% tabs %}
{% tab title="Mac" %}
```bash
$ python3 --version
# should print 3.x.x

$ python3 -m venv "venv"
```
{% endtab %}

{% tab title="Windows" %}
```bash
$ python --version
# should print 3.x.x
 
$ python -m venv "venv"
```
{% endtab %}
{% endtabs %}

{% hint style="info" %}
Download Python if you haven't already [https://www.python.org/downloads/](https://www.python.org/downloads/)
{% endhint %}

Depending on your IDE, it _should_ automatically detect that a Virtual Environment has been created and ask if it should use it. Accept :)

Otherwise, you can manually configure your IDE to use the Virtual Environment.

{% tabs %}
{% tab title="VS Code" %}
```
Install the Python extension
Open the Command Palette (CMD + SHIFT + P or CTRL + SHIFT + P)
Search for "Python: Select Interpreter"
Select the venv for your Project
```
{% endtab %}

{% tab title="PyCharm" %}
```
Open Preferences (or Settings)
Open Project > Project Interpreter
Select the venv for your Project in the Project Interpreter dropdown
Click APPLY, then OK
```
{% endtab %}
{% endtabs %}

Kill all Terminal sessions, then reopen a Terminal. It should now open and activate the Virtual Environment automatically. This is indicated by the **(venv)** prefix as seen in the example below:

{% code title="New Terminal" %}
```bash
$ (venv) python --version
# should print 3.x.x for Mac or Windows.
# Mac users don't need to use python3 or pip3 anymore!
```
{% endcode %}

{% hint style="info" %}
Real Python goes more in-depth on their website: [Virtual Environments](https://realpython.com/python-virtual-environments-a-primer/)
{% endhint %}
