---
description: The first step in contributing to Pylenium.io
---

# Clone and Setup the Project

## 1. Fork the Project

This GitHub Guide is simple and concise! It goes over:

* How to Fork
* Clone and add to your Fork
* Submitting a Pull Request \(PR\)

{% embed url="https://guides.github.com/activities/forking/" caption="" %}

## 2. Virtual Environment

Once cloned, open your IDE of choice and create a Virtual Environment.

{% hint style="info" %}
Follow the Pylenium guide for venvs and pytest here: [Virtual Environments](../getting-started/virtual-environments.md)
{% endhint %}

## 3. Package Management with Pipenv

Pipenv is the package manager that is used for Pylenium. Please take a moment to read this guide to understand how to use it and the Pipfiles.

{% embed url="https://realpython.com/pipenv-guide/" caption="" %}

### Install pipenv globally

{% tabs %}
{% tab title="Mac \| Linux" %}
```text
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
You must be using **Python 3.8.1** or greater!
{% endhint %}

## 4. Follow our Contributing Guide

You're all set! Head on over to our [CONTRIBUTING GUIDE](https://github.com/ElSnoMan/pyleniumio/tree/d887dd0028538e9416fe3fe284a75ab30a2dc744/CONTRIBUTING.md) for more information on:

* Code of Conduct
* Templates for Bugs, Enhancements, etc.
* Guidelines for Pull Requests and suggestions
* and more!

Thank you for taking the time to contribute! We're excited to have you!

