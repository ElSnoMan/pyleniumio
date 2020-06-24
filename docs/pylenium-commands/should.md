---
description: A collection of expectations for the current driver.
---

# should

## Expectations

* `.contain_title()`
* `.contain_url()`
* `.have_title()`
* `.have_url()`
* `.not_find()`
* `.not_find_xpath()`
* `.not_contain()`

## Syntax

```python
# use the default wait_time
py.should().<expectation>

---or---

# customize the wait_time for this expectation
py.should(timeout).<expectation>

---or---

# ignore exceptions that you expect to "get in the way"
py.should(ignored_exceptions).<expectation>

---or---

# customize both fully
py.should(timeout, ignored_exceptions).<expectation>
```

## Usage

{% code title="correct usage" %}
```python
py.visit('https://qap.dev').should().have_title('QA at the Point')
```
{% endcode %}

## Arguments

* `.contain_title(string)` - The substring for the title to contain
* `.contain_url(string)` - The substring for the URL to contain
* `.have_title(title)` - The case-sensitive title to match
* `.have_url(url)` - The case-sensitive url to match
* `.not_find(css)` - The CSS selector
* `.not_find_xpath(xpath)` - The XPATH selector
* `.not_contain(text)` - The text to contain

## Yields

* **\(Pylenium\)** If the assertion passes, then the current instance of Pylenium is returned, else an **AssertionError** is raised if the condition is not met within the specified timeout.
* **\(Bool\)** for the Find Element expectations.

