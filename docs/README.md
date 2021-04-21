---
description: Web Test Automation made easy
---

# Welcome to the Pylenium.io Docs

[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](https://github.com/ElSnoMan/pyleniumio/tree/0bd684d227127daf2eccd2f284b849d4a91e3cb5/docs/code_of_conduct.md)

## Welcome to the Pylenium.io Docs

### The mission is simple

> Bring the best of Selenium, Cypress and Python into one package.

This means:

* Automatic waiting and synchronization
* Quick setup to start writing tests
* Easy to use and clean syntax for amazing readability and maintainability
* Automatic driver installation so you don't need to manage drivers
* Leverage the awesome Python language
* and more!

#### Test Example

Let's use this simple scenario to show the difference between using `Selenium` and `Pylenium`:

1. **Visit** the QA at the Point website: [https://qap.dev](https://qap.dev/)
2. **Hover** the About link to reveal a menu
3. **Click** the Leadership link in that menu
4. **Assert** Carlos Kidman is on the Leadership page

{% code title="Using Pylenium" %}
```python
def test_carlos_is_on_leadership(py):
    py.visit('https://qap.dev')
    py.get('a[href="/about"]').hover()
    py.get('a[href="/leadership"][class^="Header-nav"]').click()
    assert py.contains('Carlos Kidman')
```
{% endcode %}

{% code title="The same test using Selenium" %}
```python
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# define your setup and teardown fixture
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_carlos_is_on_leadership_page_with_selenium(driver):
    wait = WebDriverWait(driver, timeout=10)
    driver.get('https://qap.dev')

    # hover About link
    about_link = driver.find_element(By.CSS_SELECTOR, "a[href='/about']")
    actions = ActionChains(driver)
    actions.move_to_element(about_link).perform()

    # click Leadership link in About menu
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/leadership'][class^='Header-nav']"))).click()

    # check if 'Carlos Kidman' is on the page
    assert wait.until(lambda _: driver.find_element(By.XPATH, "//*[contains(text(), 'Carlos Kidman')]"))
```
{% endcode %}

#### Purpose

I teach courses and do trainings for both **Selenium** and **Cypress**, but Selenium, out of the box, _feels_ clunky. When you start at a new place, you almost always need to "setup" the framework from scratch all over again. Instead of getting right to creating meaningful tests, you end up spending most of your time building a custom framework, maintaining it, and having to teach others to use it.

Also, many people blame Selenium for bad or flaky tests. This usually tells me that they have yet to experience someone that truly knows how to make Selenium amazing! This also tells me that they are not aware of the usual root causes that make Test Automation fail:

* Poor programming skills, test design and practices
* Flaky applications
* Complex frameworks

What if we tried to get the best from both worlds and combine it with an amazing language?

**Selenium** has done an amazing job of providing W3C bindings to many languages and makes scaling a breeze.

**Cypress** has done an amazing job of making the testing experience more enjoyable - especially for beginners.

**Pylenium** looks to bring more Cypress-like bindings and techniques to Selenium \(like automatic waits\) and still leverage Selenium's power along with the ease-of-use and power of **Python**.

### Quick Start

{% hint style="success" %}
If you are new to Selenium or Python, do the [Getting Started steps 1-4](getting-started/virtual-environments.md)
{% endhint %}

You can also watch the Getting Started video with Pylenium's creator, Carlos Kidman!

{% embed url="https://www.youtube.com/watch?v=li1nc4SUojo" caption="Getting Started with v1.7.7+" %}

{% hint style="success" %}
You don't need to worry about installing any driver binaries like `chromedriver`. **Pylenium** does this all for you automatically :\)
{% endhint %}

#### 1. Install **pyleniumio**

{% code title="Terminal $" %}
```python
pip install pyleniumio

---or---

pipenv install pyleniumio
```
{% endcode %}

#### 2. Initialize Pylenium

{% code title="Terminal $ " %}
```text
pylenium init
```
{% endcode %}

{% hint style="success" %}
Execute this command at your Project Root
{% endhint %}

This creates three files:

* `conftest.py` - This has the fixtures needed for Pylenium.
* `pylenium.json` - This is the [configuration ](https://github.com/ElSnoMan/pyleniumio/blob/master/docs/configuration/pylenium.json.md)file for Pylenium.
* `pytest.ini` - This is the configuration file for pytest and is used to connect to [ReportPortal](https://github.com/ElSnoMan/pyleniumio/blob/master/docs/configuration/report-portal.md)

By default, Pylenium uses Chrome browser. You have to install Chrome or update the `pylenium.json` file to use the browser of your choice.

#### 3. Write a test

Create a directory called `tests` and then a test file called `test_google.py`

Define a new test called `test_google_search`

{% code title="test\_google.py" %}
```python
def test_google_search(py)
```
{% endcode %}

{% hint style="info" %}
Pylenium uses **pytest** as the Test Framework. You only need to pass in `py`to the function!
{% endhint %}

Now we can use **Pylenium Commands** to interact with the browser.

{% code title="test\_google.py" %}
```python
def test_google_search(py):
    py.visit('https://google.com')
    py.get("[name='q']").type('puppies')
    py.get("[name='btnK']").submit()
    assert py.should().contain_title('puppies')
```
{% endcode %}

#### 4. Run the Test

This will depend on your IDE, but you can always run tests from the CLI:

{% code title="Terminal $ \(venv\)" %}
```bash
python -m pytest tests/test_google.py
```
{% endcode %}

You're all set! You should see the browser open and complete the commands we had in the test :\)
