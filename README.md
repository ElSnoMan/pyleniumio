---
description: Web Test Automation made easy
---

# Welcome to Pylenium

<figure><img src=".gitbook/assets/pylenium-banner.png" alt=""><figcaption></figcaption></figure>

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
    py.visit("https://qap.dev")
    py.get("a[href='/about']").hover()
    py.get("a[href='/leadership'][class^='Header-nav']").click()
    assert py.contains("Carlos Kidman")
```
{% endcode %}

{% code title="The same test using Selenium" %}
```python
# Define your setup and teardown fixture
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_carlos_is_on_leadership(driver):
    wait = WebDriverWait(driver, timeout=10)
    driver.get("https://qap.dev")

    # Hover About link
    about_link = driver.find_element(By.CSS_SELECTOR, "a[href='/about']")
    actions = ActionChains(driver)
    actions.move_to_element(about_link).perform()

    # Click Leadership link in About menu
    wait.until(EC.element_visible(By.CSS_SELECTOR, "a[href='/leadership'][class^='Header-nav']")).click()

    # Check if 'Carlos Kidman' is on the page
    assert wait.until(lambda _: driver.find_element(By.XPATH, "//*[contains(text(), 'Carlos Kidman')]"))
```
{% endcode %}

#### Purpose

I teach courses and do trainings for **Selenium,** **Cypress, and Playwright**, but Selenium, out of the box, _feels_ clunky. When you start at a new place, you almost always need to "setup" the framework from scratch all over again. Instead of getting right to creating meaningful tests, you end up spending most of your time building a custom framework, maintaining it, and having to teach others to use it.

Also, many people blame Selenium for bad or flaky tests. This usually tells me that they have yet to experience someone that truly knows how to make Selenium amazing! This also tells me that they are not aware of the usual root causes that make Test Automation fail:

* Poor programming skills, test design, and practices
* Flaky applications
* Complex frameworks

What if we tried to get the best from both worlds and combine it with a fantastic language?

**Selenium** has done an amazing job of providing W3C bindings to many languages, making scaling a breeze. W3C is the standard for the web, so leveraging it just makes sense.

**Cypress** has done an amazing job of making the testing experience more enjoyable - especially for beginners. It's easy to start with and the API is readable and flows nicely.

**Pylenium** looks to bring more Cypress-like bindings and techniques to Selenium (like automatic waits) and still leverage Selenium's power along with the ease of use and power of **Python**.

### Quick Start

{% hint style="success" %}
If you are new to Selenium or Python, do the [Getting Started steps 1-4](docs/getting-started/virtual-environments.md)
{% endhint %}

You can also watch the Getting Started video with Pylenium's creator, Carlos Kidman!

{% embed url="https://www.youtube.com/watch?v=li1nc4SUojo" %}
Getting Started with v1.7.7+
{% endembed %}

{% hint style="success" %}
You don't need to worry about installing any driver binaries like `chromedriver`. **Pylenium** does this all for you automatically :)
{% endhint %}

#### 1. Install **pyleniumio**

{% code title="Terminal $" %}
```python
pip install pyleniumio

---or---

pipenv install pyleniumio

---or---

poetry add pyleniumio
```
{% endcode %}

#### 2. Initialize Pylenium

{% code title="Terminal $ " %}
```
pylenium init
```
{% endcode %}

{% hint style="success" %}
Execute this command at your Project Root
{% endhint %}

This creates three files:

* <mark style="color:yellow;">**`conftest.py`**</mark> - This has the fixtures needed for Pylenium
* <mark style="color:yellow;">**`pylenium.json`**</mark> - This is the [configuration ](docs/configuration/pylenium.json.md)file for Pylenium
* <mark style="color:yellow;">**`pytest.ini`**</mark> - This is the configuration file for pytest

By default, Pylenium uses the Chrome browser. You have to install Chrome or update the `pylenium.json` file to use the browser of your choice.

#### 3. Write a test

Create a directory called `tests` and then a test file called `test_google.py`

Define a new test called `test_google_search`

{% code title="test_google.py" %}
```python
def test_google_search(py)
```
{% endcode %}

{% hint style="info" %}
Pylenium uses <mark style="color:yellow;">**pytest**</mark> as the Test Framework. You only need to pass in `py`to the function!
{% endhint %}

Now we can use <mark style="color:yellow;">**Pylenium Commands**</mark> to interact with the browser.

{% code title="test_google.py" %}
```python
from pylenium.driver import Pylenium

def test_google_search(py: Pylenium):
    py.visit('https://google.com')
    py.get("[name='q']").type('puppies')
    py.get("[name='btnK']").submit()
    assert py.should().contain_title('puppies')
```
{% endcode %}

{% hint style="info" %}
Some IDEs, like PyCharm, auto-detect pytest fixtures and provide intellisense and autocomplete.
{% endhint %}

#### 4. Run the Test

This will depend on your IDE, but you can always run tests from the CLI:

{% code title="Terminal $ (venv)" %}
```bash
pytest tests/test_google.py
```
{% endcode %}

You're all set! You should see the browser open and complete the commands we had in the test :)
