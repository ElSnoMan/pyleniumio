---
description: A collection of expected conditions against the current browser.
---

# ⏱ Driver.should()

## Expectations

* <mark style="color:purple;">`.contain_title(title: str)`</mark> - The substring for the title to contain
* <mark style="color:purple;">`.contain_url(url: str)`</mark> - The substring for the URL to contain
* <mark style="color:purple;">`.have_title(title: str)`</mark> - The case-sensitive title to match
* <mark style="color:purple;">`.have_url(url: str)`</mark> - The case-sensitive url to match
* <mark style="color:purple;">`.not_find(css: str)`</mark> - The CSS selector
* <mark style="color:purple;">`.not_findx(xpath: str)`</mark> - The XPATH selector
* <mark style="color:purple;">`.not_contain(text: str)`</mark> - The text to contain

## Syntax

```python
# Use the default wait_time
py.should().<expectation>

---or---

# Customize the wait_time for this expectation
py.should(timeout: int).<expectation>

---or---

# Ignore exceptions that you expect to "get in the way"
py.should(ignored_exceptions: list).<expectation>

---or---

# Customize both fully
py.should(timeout: int, ignored_exceptions: list).<expectation>
```

## Examples

{% code title=".contain_title()" %}
```python
def test_title_contains(py):
    py.visit("https://qap.dev")
    assert py.should().contain_title("QA")
```
{% endcode %}

{% code title=".contain_url()" %}
```python
def test_url_contains(py):
    py.visit("https://qap.dev")
    assert py.should().contain_url("www.qap.dev")
```
{% endcode %}

{% code title=".have_title()" %}
```python
def test_title_matches(py):
    py.visit("https://qap.dev")
    assert py.should().have_title("QA at the Point")
```
{% endcode %}

{% code title=".have_url()" %}
```python
def test_url_matches(py):
    py.visit("https://qap.dev")
    assert py.should().have_title("https://www.qap.dev/")
```
{% endcode %}

{% code title=".not_find()" %}
```python
def test_page_does_not_have_element(py):
    py.visit("https://qap.dev")
    assert py.should().not_find("#zaboomafoo")
```
{% endcode %}

{% code title=".not_findx()" %}
```python
def test_page_does_not_have_element(py):
    py.visit("https://qap.dev")
    assert py.should().not_findx("//*[@id='zaboomafoo']")
```
{% endcode %}

{% code title=".not_contain()" %}
```python
def test_text_should_not_be_present_on_page(py):
    py.visit("https://qap.dev")
    assert py.should().not_contain("zaboomafoo")
```
{% endcode %}

{% code title="Customize timeout" %}
```python
def test_title_matches_within_5_seconds(py):
    py.visit("https://qap.dev")
    # Override global timeout for only this action
    assert py.should(timeout=5).have_title("QA at the Point")
```
{% endcode %}

{% code title="Ignore exceptions" %}
```python
def test_title_matches(py):
    py.visit("https://qap.dev")
    # These exceptions will not stop the "wait until"
    exceptions = [WebDriverException, NoSuchElementException]
    assert py.should(ignored_exceptions=exceptions).have_title("QA at the Point")
```
{% endcode %}



## Yields

* <mark style="color:orange;">**Pylenium**</mark> - If the assertion passes, then the current instance of Pylenium is returned, else an **AssertionError** is raised if the condition is not met within the specified timeout.
* **bool** - for the Find Element expectations.
