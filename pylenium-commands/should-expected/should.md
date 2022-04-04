---
description: A collection of expected conditions against the current browser.
---

# ⏱ Pylenium.should()

## Expectations

* `.contain_title(title: str)` - The substring for the title to contain
* `.contain_url(url: str)` - The substring for the URL to contain
* `.have_title(title: str)` - The case-sensitive title to match
* `.have_url(url: str)` - The case-sensitive url to match
* `.not_find(css: str)` - The CSS selector
* `.not_findx(xpath: str)` - The XPATH selector
* `.not_contain(text: str)` - The text to contain

## Syntax

```python
# use the default wait_time
py.should().<expectation>

---or---

# customize the wait_time for this expectation
py.should(timeout: int).<expectation>

---or---

# ignore exceptions that you expect to "get in the way"
py.should(ignored_exceptions: list).<expectation>

---or---

# customize both fully
py.should(timeout: int, ignored_exceptions: list).<expectation>
```

## Examples

{% code title=".contain_title()" %}
```python
def test_title_contains(py):
    py.visit('https://qap.dev')
    assert py.should().contain_title('QA')
```
{% endcode %}

{% code title=".contain_url()" %}
```python
def test_url_contains(py):
    py.visit('https://qap.dev')
    assert py.should().contain_url('www.qap.dev')
```
{% endcode %}

{% code title=".have_title()" %}
```python
def test_title_matches(py):
    py.visit('https://qap.dev')
    assert py.should().have_title('QA at the Point')
```
{% endcode %}

{% code title=".have_url()" %}
```python
def test_url_matches(py):
    py.visit('https://qap.dev')
    assert py.should().have_title('https://www.qap.dev/')
```
{% endcode %}

{% code title=".not_find()" %}
```python
def test_page_does_not_have_element(py):
    py.visit('https://qap.dev')
    assert py.should().not_find('#zaboomafoo')
```
{% endcode %}

{% code title=".not_findx()" %}
```python
def test_page_does_not_have_element(py):
    py.visit('https://qap.dev')
    assert py.should().not_findx('//*[@id="zaboomafoo"]')
```
{% endcode %}

{% code title=".not_contain()" %}
```python
def test_text_should_not_be_present_on_page(py):
    py.visit('https://qap.dev')
    assert py.should().not_contain('zaboomafoo')
```
{% endcode %}

{% code title="Customize timeout" %}
```python
def test_title_matches_within_5_seconds(py):
    py.visit('https://qap.dev')
    # Override global timeout for only this action
    assert py.should(timeout=5).have_title('QA at the Point')
```
{% endcode %}

{% code title="Ignore exceptions" %}
```python
def test_title_matches(py):
    py.visit('https://qap.dev')
    # These exceptions will not stop the "wait until"
    exceptions = [WebDriverException, NoSuchElementException]
    assert py.should(ignored_exceptions=exceptions).have_title('QA at the Point')
```
{% endcode %}



## Yields

* **(Pylenium)** If the assertion passes, then the current instance of Pylenium is returned, else an **AssertionError** is raised if the condition is not met within the specified timeout.
* **(Bool)** for the Find Element expectations.
