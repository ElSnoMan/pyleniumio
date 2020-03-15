# Welcome to the Pylenium.io Docs

## The mission is simple

> Make the Selenium experience more like Cypress

I teach courses and do trainings for both **Selenium** and **Cypress**, but Selenium, out of the box, _feels_ clunky. When you start at a new place, you almost always need to "setup" the framework from scratch all over again. Instead of getting right to creating meaningful tests, you end up spending most of your time building a custom framework, maintaining it, and having to teach others to use it.

Also, many people blame Selenium for bad or flaky tests. This usually tells me that they have yet to experience someone that truly knows how to make Selenium amazing! This also tells me that they are not aware of the usual root causes that make Test Automation fail:

* Poor programming skills, test design and practices
* Flaky applications
* Complex frameworks

What if we tried to get the best from both worlds and combine it with an amazing language?

**Selenium** has done an amazing job of providing W3C bindings to many languages and makes scaling a breeze.

**Cypress** has done an amazing job of making the testing experience more enjoyable - especially for beginners.

**Pylenium** looks to bring more Cypress-like bindings and techniques to Selenium \(like automatic waits\) and still leverage Selenium's power along with the ease-of-use and power of **Python**.

## Quick Start

{% hint style="info" %}
You must be using a [**Virtual Environment**](getting-started/virtual-environments.md) in your Project
{% endhint %}

### Install the **pyleniumio** package

```
$ pip install pyleniumio
```

This will also create two files at your Workspace Root \(aka the directory outside your Virtual Environment\)

* `conftest.py`   - Ready-to-use fixtures to start writing tests immediately
* `pylenium.json` - Pylenium config settings

{% hint style="info" %}
 Pylenium uses **pytest** as the Test Framework
{% endhint %}

### Write a test

Create a directory called `tests` and then a test file called `test_google.py`

Define a new test called `test_google_search`

{% code title="test\_google.py" %}
```python
def test_google_search(py)
```
{% endcode %}

With **pytest,** you only need to pass in `py` to start using **Pylenium**!

Now we can use **Pylenium Commands** to interact with the browser.

{% code title="test\_google.py" %}
```python
def test_google_search(py):
    py.visit('https://google.com')
    py.get("[name='q']").type('puppies')
    py.get("[name='btnK']").submit()
    assert 'puppies' in py.title
```
{% endcode %}

### Install chromedriver

Everyone handles the install of their **drivers** differently.

{% hint style="info" %}
Pylenium expects your driver to be on your **PATH**
{% endhint %}

The easiest way to do this is with `WebDriver Manager`

Install the manager with Node:

```bash
$ npm install -g webdriver-manager
```

Then download the chromedriver executable:

```bash
$ webdriver-manager update
```

### Run the Test

This will depend on your IDE, but you can always run tests from the CLI:

```bash
$ python -m pytest tests/test_google.py
```

You're all set! You should see the browser open and complete the commands we had in the test :\)

