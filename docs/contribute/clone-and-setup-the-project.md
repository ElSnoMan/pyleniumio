---
description: The first step in contributing to Pylenium.io
---

# Clone and Setup the Project

## 1. Fork the Project

This GitHub Guide is simple and concise! It goes over:

* How to Fork
* Clone and add to your Fork
* Submitting a Pull Request \(PR\)

{% embed url="https://guides.github.com/activities/forking/" %}

## 2. Virtual Environment

Once cloned, open your IDE of choice and create a Virtual Environment.

{% hint style="info" %}
Follow the Pylenium guide for venvs and pytest here: [Virtual Environments](../getting-started/virtual-environments.md)
{% endhint %}

## 3. Package Management with Pipenv

Pipenv is the package manager that is used for Pylenium. Please take a moment to read this guide to understand how to use it and the Pipfiles.

{% embed url="https://realpython.com/pipenv-guide/" %}

### Install pipenv globally

{% tabs %}
{% tab title="Mac \| Linux" %}
```
pip3 install pipenv
```
{% endtab %}

{% tab title="Windows" %}
```bash
pip install pipenv
```
{% endtab %}
{% endtabs %}

### Install the packages from Pipfile

Now open a Terminal in the pyleniumio project to install the packages.

{% code title="Terminal $" %}
```bash
pipenv sync
```
{% endcode %}



{% hint style="warning" %}
You must be using **Python 3.7** or greater!
{% endhint %}

