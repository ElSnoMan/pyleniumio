# Welcome to the Pylenium.io Repo

## The mission is simple

> Bring the best of Selenium, Cypress and Python into one package.

This means:

* Automatic waiting and synchronization
* Quick setup to start writing tests
* Easy to use and clean syntax for amazing readability and maintainability
* Automatic driver installation so you don't need to manage drivers
* Leverage the awesome Python language
* and more!

Let's use this simple scenario to show the difference between using `Selenium` and `Pylenium`:

1. Visit the QA at the Point website: https://qap.dev
2. Hover the About link to reveal a menu
3. Click the Leadership link in that menu
4. Assert Carlos Kidman is on the Leadership page

### Here is the test using Pylenium:

```python
def test_carlos_is_on_leadership(py):
    py.visit('https://qap.dev')
    py.get('a[href="/about"]').hover()
    py.get('a[href="/leadership"][class^="Header-nav"]').click()
    assert py.contains('Carlos Kidman')
```

### Here is the same test with Selenium:

```python
# define your setup and teardown fixture
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_carlos_is_on_leadership_page_with_selenium(driver):
    driver.get('https://qap.dev')
    
    # hover About link
    about_link = driver.find_element(By.CSS_SELECTOR, "a[href='/about']")
    actions = ActionChains(driver)
    actions.move_to_element(about_link).perform()
    
    # click Leadership link in About menu
    driver.find_element(By.CSS_SELECTOR, "a[href='/leadership'][class^='Header-nav']").click()
    
    # check if 'Carlos Kidman' is on the page
    assert driver.find_element(By.XPATH, "//*[contains(text(), 'Carlos Kidman')]")
```

## Purpose

I teach courses and do trainings for both **Selenium** and **Cypress**, but Selenium, out of the box, _feels_ clunky. When you start at a new place, you almost always need to "setup" the framework from scratch all over again. Instead of getting right to creating meaningful tests, you end up spending most of your time building a custom framework, maintaining it, and having to teach others to use it.

Also, many people blame Selenium for bad or flaky tests. This usually tells me that they have yet to experience someone that truly knows how to make Selenium amazing! This also tells me that they are not aware of the usual root causes that make Test Automation fail:

* Poor programming skills, test design and practices
* Flaky applications
* Complex frameworks

What if we tried to get the best from both worlds and combine it with an amazing language?

**Selenium** has done an amazing job of providing W3C bindings to many languages and makes scaling a breeze.

**Cypress** has done an amazing job of making the testing experience more enjoyable - especially for beginners.

**Pylenium** looks to bring more Cypress-like bindings and techniques to Selenium \(like automatic waits\) and still leverage Selenium's power along with the ease-of-use and power of **Python**.

## Visit the Docs

Our gitbook docs have everything you need to know about Pylenium: https://elsnoman.gitbook.io/pylenium/
