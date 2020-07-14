---
description: pytest uses specific naming conventions and project structure
---

# 3. Project Structure with pytest

## Pylenium Files

You should have created these in the previous step, but they are required for **Pylenium** to do its magic.

* `conftest.py`
* `pylenium.json`
* `pytest.ini`

{% hint style="success" %}
Make sure these are at the Project Root \(aka Workspace\)
{% endhint %}

## conftest.py

pytest uses special functions called **Fixtures** to control the **Setup** and **Teardown** of tests and runs.

{% hint style="danger" %}
If you put any other **custom** functions or fixtures in this **conftest.py**, they will be _overridden_ when you upgrade Pylenium
{% endhint %}

### Fixture Example

```python
import pytest

@pytest.fixture
def user():
    new_user = user_service.create()
    yield new_user
    user_service.delete(new_user)
```

* `@pytest.fixture` - this decorator indicates that this function has a Setup and Teardown 
* `def user():` - define the function like normal. `user` will be the name of the fixture to be used in tests
* Everything _before_ the `yield` is executed before each test
* `yield new_user` - returns `new_user` and gives control back to the test. The rest of the function is not executed yet
* Everything _after_ the `yield` is executed after each test

### Use the Fixture

{% code title="test\_\*.py file" %}
```bash
def test_my_website(py, login, user):
    py.visit('https://qap.dev')
    login.with(user)
    ...
```
{% endcode %}

When this test is ran:

1. test - The test looks at its parameter list and calls the `py` fixture
2. fixture - `user` yields the newly created user
3. test - line 2 is executed by navigating to `https://qap.dev` and then logging in with the new user
4. fixture - test is complete \(doesn't matter if it passes or fails\) and `user_service.delete_user()` is executed

### Folder Structure

The `conftest.py` file is used to _store_ fixtures and make them available to any tests in their **Scope**.

{% hint style="info" %}
**Scope** refers to the file's siblings and their descendants.
{% endhint %}

Take a look at the following Project Structure

* Project
  * conftest.py  \# 1
  * pylenium.json
  * api\_tests
    * conftest.py  \# 2 
    * test\_rest\_api.py
  * ui\_tests
    * conftest.py  \# 3
    * test\_google.py

`test_google.py` would have access to fixtures in `conftest.py #1` and `conftest.py #3`

`test_rest_api.py` would have access to fixtures in `conftest.py #1` and `conftest.py #2`

## Test Naming Conventions

By now it might be obvious that pytest has specific naming conventions by default.

### Folders and Files

* You may want to store your tests in a `/tests` directory \(optional\)
* You may want to make files easily identified as test files, so use `test_*.py` \(optional\)

{% hint style="info" %}
These techniques help you and the Test Runner discover/find and execute your tests more easily, but they are not required. Do what works best for you and your team.
{% endhint %}

**pytest** can run tests based off of directories or files, so you can group tests into **Suites** this way.

* Project
  * tests
    * ui
      * test\_login.py
      * test\_checkout.py
    * api
      * test\_payment.py
      * test\_user.py
    * unit

```bash
# run all tests
$ python -m pytest tests

# run tests in ui directory
$ python -m pytest tests/ui

# run only the payment api tests
$ python -m pytest tests/api/test_payment.py
```

### Classes

You _can_ group tests into Suites using Classes.

{% hint style="danger" %}
This is not the recommended approach for beginners
{% endhint %}

```python
def TestCheckout:

    def test_with_visa(self, py):
        # test code
    
    def test_with_mastercard(self, py):
        # test code
```

* The class must start with the word `Test`
* Test functions must have `self` as their first parameter \(since they are in a class\)

{% hint style="info" %}
You can have as many Test Classes and Test Functions as you want in a file
{% endhint %}

### Test Functions

Tests do NOT need to be in a Test Class. They can exist by themselves in a file and makes the tests and overall file look much cleaner.

{% hint style="success" %}
RECOMMEND this approach for working with Pylenium for beginners and everyone else really
{% endhint %}

{% code title="test\_checkout.py" %}
```python
def test_with_visa(py):
    # test_code
    
def test_with_mastercard(py):
    # test_code
```
{% endcode %}

* Test names must start with `test_`, but can have anything else after that

{% hint style="danger" %}
Tests should not _share_ **data** or **state**.
{% endhint %}

{% hint style="success" %}
Tests should be **modular**, **deterministic** and **meaningful**
{% endhint %}

Pylenium is architected in a way that makes test design easy and intuitive, but also gives you a lot of things for free. **The framework is already designed to be scaled with containerized solutions like Docker and Kubernetes.**

