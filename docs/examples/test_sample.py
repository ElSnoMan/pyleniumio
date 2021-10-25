""" Examples will be added to this directory and its files.

However, the best source for info and details is in the
official documentation here:

https://elsnoman.gitbook.io/pylenium

You can also contact the author, @CarlosKidman
on Twitter or LinkedIn.
"""

# You can mix Selenium into some Pylenium commands
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


# pass in the `py` fixture into your test function
# this _is_ Pylenium!
def test_pylenium_basics(py):
    # Use Cypress-like commands like `.visit()`
    py.visit("https://google.com")
    # `.get()` uses CSS to locate a single element
    py.get('[name="q"]').type("puppies", py.Keys.ENTER)
    # `assert` followed by a boolean expression
    assert "puppies" in py.title


def test_access_selenium(py):
    py.visit("https://google.com")
    # access the wrapped WebDriver with `py.webdriver`
    search_field = py.webdriver.find_element(By.CSS_SELECTOR, "[name='q']")
    # access the wrapped WebElement with `Element.webelement`
    assert py.get('[name"q"]').webelement.is_enabled()
    # you can store elements and objects to be used later since
    # we don't rely on Promises or chaining in Python
    search_field.send_keys("puppies", py.Keys.ENTER)
    assert "puppies" in py.title


def test_chaining_commands(py):
    py.visit("https://google.com").get('[name="q"]').type("puppies", py.Keys.ENTER)
    assert "puppies" in py.title


def test_waiting(py):
    py.visit("https://google.com")
    # wait using expected conditions
    # default `.wait()` uses WebDriverWait which returns Selenium's WebElement objects
    py.wait().until(ec.visibility_of_element_located((By.CSS_SELECTOR, '[name="q"]'))).send_keys("puppies")
    # use_py=True to use a PyleniumWait which returns Pylenium's Element and Elements objects
    py.wait(use_py=True).until(lambda _: py.get('[name="q"]')).type(py.Keys.ENTER)
    # wait using lambda function
    assert py.wait().until(lambda x: "puppies" in x.title)
