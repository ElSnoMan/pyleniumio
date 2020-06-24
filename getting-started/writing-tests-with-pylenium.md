---
description: Easy as py
---

# 4. Writing Tests with Pylenium

## Create a Test File

A **Test File** is just that - a file with tests in it. Depending on the type of project you're working on, you may want these to live right next to your code files or in a separate `/tests` directory.

{% hint style="info" %}
In these docs we will assume you are writing your tests in a `/tests` directory of your project.
{% endhint %}

Create a Test File called `test_qap_dev.py`

* Test Files do not need to start with `test_`
* This is a naming convention used to make it easier to distinguish between code and tests

You should now have a Project Structure that looks like this:

* Project
  * tests
    * test\_qap\_dev.py
  * conftest.py
  * venv

## Write the Test

We are going to make a test that does the following:

1. _Visits_ the **QA at the Point** website: [https://qap.dev](https://qap.dev)
2. _Hovers_ the **About** link to reveal a menu
3. _Click_ the **Leadership** link in that menu
4. _Assert_ **Carlos Kidman** is on the Leadership page

{% code title="test\_qap\_dev.py" %}
```python
def test_carlos_is_on_leadership(py):
    py.
```
{% endcode %}

When you type `py.`, you should see an **auto-complete** or **IntelliSense** menu appear with the list of [Pylenium Commands](../pylenium-commands/commands.md) like `.visit()` and `.get()`

{% hint style="warning" %}
 Your IDE may not do this or you may be missing an Extension or Plugin.

PyCharm has [pytest support](setup-pytest.md) out-of-the-box.
{% endhint %}

Let's move on with the steps.

* Visit [https://qap.dev](https://qap.dev)

{% code title="test\_qap\_dev.py" %}
```bash
def test_carlos_is_on_leadership(py):
    py.visit('https://qap.dev')
```
{% endcode %}

* Hover the **About** link to reveal a menu

{% code title="test\_qap\_dev.py" %}
```python
def test_carlos_is_on_leadership(py):
    py.visit('https://qap.dev')
    py.get('a[href="/about"]').hover()
```
{% endcode %}

{% hint style="info" %}
When you get an element from locators \( `.get()`, `.contains()`, `.find()`, or `.xpath()`\), you can perform actions against the element like `.click()`, `.type()` and `.hover()`
{% endhint %}

* Click the **Leadership** link in the menu

{% code title="test\_qap\_dev.py" %}
```python
def test_carlos_is_on_leadership(py):
    py.visit('https://qap.dev')
    py.get('a[href="/about"]').hover()
    py.get('a[href="/leadership"][class^="Header-nav"]').click()
```
{% endcode %}

* Assert **Carlos Kidman** is on the Leadership page

{% code title="test\_qap\_dev.py" %}
```python
def test_carlos_is_on_leadership(py):
    py.visit('https://qap.dev')
    py.get('a[href="/about"]').hover()
    py.get('a[href="/leadership"][class^="Header-nav"]').click()
    assert py.contains('Carlos Kidman')
```
{% endcode %}

## Run the Test

If you're using PyCharm, there should be a green **Play** button next to the test definition. Click it and select either **Run** to execute normally or **Debug** to use breakpoints in Debug Mode.

Otherwise, use the method your IDE provides. You can always use the CLI as well:

{% code title="Terminal $ \(venv\)" %}
```bash
python -m pytest tests/test_qap_dev.py
```
{% endcode %}

### Look at the Difference

Here is the same test but written with Selenium out of the box:

```bash
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



