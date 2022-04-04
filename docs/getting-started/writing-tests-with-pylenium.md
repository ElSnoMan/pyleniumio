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

{% code title="test_qap_dev.py" %}
```python
def test_carlos_is_on_leadership(py):
    py.
```
{% endcode %}

When you type `py.`, you should see an **auto-complete** or **IntelliSense** menu appear with the list of [Pylenium Commands](../pylenium-commands/commands.md) like `.visit()` and `.get()`

{% hint style="warning" %}
&#x20;Your IDE may not do this or you may be missing an Extension or Plugin.

PyCharm has [pytest support](setup-pytest.md) out-of-the-box.
{% endhint %}

Let's move on with the steps.

* Visit [https://qap.dev](https://qap.dev)

{% code title="test_qap_dev.py" %}
```bash
def test_carlos_is_on_leadership(py):
    py.visit('https://qap.dev')
```
{% endcode %}

* Hover the **About** link to reveal a menu

{% code title="test_qap_dev.py" %}
```python
def test_carlos_is_on_leadership(py):
    py.visit('https://qap.dev')
    py.get('a[href="/about"]').hover()
```
{% endcode %}

{% hint style="info" %}
When you get an Element from locator methods:

* `.get()  | .getx()`
* `.find() | .findx()`
* `.contains()`

you can perform actions against the element like:

* `.click()`
* `.type()`
* `.hover()`
* `and more!`
{% endhint %}

{% hint style="success" %}
Make sure to check out the many commands available in Pylenium
{% endhint %}

* Click the **Leadership** link in the menu

{% code title="test_qap_dev.py" %}
```python
def test_carlos_is_on_leadership(py):
    py.visit('https://qap.dev')
    py.get('a[href="/about"]').hover()
    py.get('a[href="/leadership"][class^="Header-nav"]').click()
```
{% endcode %}

* Assert **Carlos Kidman** is on the Leadership page

{% code title="test_qap_dev.py" %}
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

{% code title="Terminal $ (venv)" %}
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

## Another Test Example

Let's write another test that searches for `Pylenium` and makes sure the results page contains that term in the title.

1. Navigate to Google.com
2. Type `Pylenium` into the search field
3. Submit the search
4. Assert the results page contains the title

```python
def test_google_search(py):
    py.visit('https://google.com')
    py.get('[name="q"]').type('Pylenium')
    py.get('[name="btnK"]').submit()
    assert py.should().contain_title('Pylenium')
```

You've already seen different Element commands like `.visit()`, `.type()` and `.submit()`,  but there is also a _Should_ object for:

* [Element](../../pylenium-commands/should-expected/should-1.md)
* [Elements](../../pylenium-commands/should-expected/should-1.md)
* [Pylenium](../../pylenium-commands/should-expected/should.md)

In the example above, `py.should()` uses an Explicit Wait to wait until the "driver" detects that the current page's title contains `"Pylenium"`.&#x20;

* If the title contains `"Pylenium"` within the specified timeout, then it returns `True` and passes the assertion
* If the title does not meet the expectation within the specified timeout, then it returns `False` and fails the assertion

{% hint style="success" %}
You can leverage these _Should_ expectations to easily wait for conditions or write assertions!
{% endhint %}
