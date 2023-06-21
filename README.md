# Pylenium: Easy Python Web Test Automation

- [The Mission](#the-mission-is-simple)
    - [Test Example](#test-example)
    - [Purpose](#purpose)
- [Quickstart](#quick-start)
    - [1. Install](#1-install-pyleniumio)
    - [2. Initialize](#2-initialize-pylenium)
    - [3. Write a Test](#3-write-a-test)
    - [4. Run the Test](#4-run-the-test)
- [Contribute](#contribute)


## The mission is simple

> Bring the best of Selenium, Cypress and Python into one package.

This means:

* Automatic waiting and synchronization
* Quick setup to start writing tests
* Easy to use and clean syntax for amazing readability and maintainability
* Automatic driver installation so you don't need to manage drivers
* Leverage the awesome Python language
* and more!

### Test Example

Although Pylenium is a thin wrapper of Selenium, let's use this simple scenario to show the difference between using `Selenium` and `Pylenium`:

1. **Visit** the QA at the Point website: [https://qap.dev](https://qap.dev/)
2. **Hover** the About link to reveal a menu
3. **Click** the Leadership link in that menu
4. **Assert** Carlos Kidman is on the Leadership page

```python
def test_carlos_is_on_leadership(py):
    py.visit('https://qap.dev')
    py.get('a[href="/about"]').hover()
    py.get('a[href="/leadership"][class^="Header-nav"]').click()
    assert py.contains('Carlos Kidman')
```

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

### Purpose

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

The [Official Pylenium Docs](https://elsnoman.gitbook.io/pylenium) are the best place to start, but you can quickly get going with the following steps:

### 1. Install **pyleniumio**

```python
pip install pyleniumio

---or---

pipenv install pyleniumio

---or---

poetry add pyleniumio
```

### 2. Initialize Pylenium

```bash
# execute at your Project Root
pylenium init
```

This creates three files:

* `conftest.py` - This has the fixtures needed for Pylenium
* `pylenium.json` - This is the config file for Pylenium
* `pytest.ini` - This is the config file for pytest

By default, Pylenium uses the Chrome browser. You have to install Chrome or update the `pylenium.json` file to use the browser of your choice.

### 3. Write a test

Create a directory called `tests` and then a test file called `test_google.py`

Define a new test called `test_google_search`

```python
def test_google_search(py)
```

Pylenium uses **pytest** as the Test Framework. You only need to pass in `py`to the function!

Now we can use **Pylenium Commands** to interact with the browser.

```python
def test_google_search(py):
    py.visit('https://google.com')
    py.get("[name='q']").type('puppies')
    py.get("[name='btnK']").submit()
    assert py.should().contain_title('puppies')
```

### 4. Run the Test

This will depend on your IDE, but you can always run tests from the CLI:

```bash
python -m pytest tests/test_google.py
```

You're all set! You should see the browser open and complete the commands we had in the test :\)

## Contribute

Pylenium uses [Gitpod](https://gitpod.io/) to make it easy to work on it from the _desktop or browser_ without having to worry about the setup like having the correct Python version installed after cloning the repo.

> 💡 With a single click, you can open the repo in your browser, make your changes, then submit a pull request!

0. If you're new to Gitpod, check out their [Getting Started](https://www.gitpod.io/docs/introduction/getting-started) docs to see how to use it
1. Visit [Pylenium's repo](https://github.com/ElSnoMan/pyleniumio) and click the `Gitpod` button to open the repo in a VS Code browser window
2. Wait for Gitpod to set up the project. You'll see things get setup from the various `.gitpod*` files at the Project Root
3. Once complete, create a new branch and start making your changes
4. When ready, submit a Pull Request!
5. Reviewers will see your CI pipeline and even be able to open your Gitpod instance if needed - making collaboration much easier
6. Gitpod instances are ephemeral, so you can create, share, and delete them as needed

> 🧪 By default, UI tests executed in Gitpod are headless. If you'd like to see UI tests run, open port `6080` from the bottom right corner of VS Code.

For more details and other ways to contribute to Pylenium, visit the [CONTRIBUTING.md](/CONTRIBUTING.md) doc 👀
