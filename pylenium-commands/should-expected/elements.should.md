---
description: A collection of expected conditions against a list of Elements
---

# ⏱ Elements.should()

## Expectations

### Positive Conditions

* `.be_empty()`
* `.have_length(length: int)`
* `.be_greater_than(length: int)`
* `.be_less_than(length: int)`

### Negative Conditions

* `.not_be_empty()`

## Syntax

```python
# use the default wait_time
Elements.should().<expectation>

---or---

# customize the wait_time for this expectation
Elements.should(timeout: int).<expectation>

---or---

# ignore exceptions that you expect to "get in the way"
Elements.should(ignored_exceptions: list).<expectation>

---or---

# customize both fully
Elements.should(timeout: int, ignored_exceptions: list).<expectation>
```

## Examples

{% code title=".has_length()" %}
```python
def test_about_menu_has_3_links(py):
    py.visit('https://qap.dev')
    about = py.get('a[href="/about"]')
    about.hover()
    assert about.find("a").should().have_length(3)
```
{% endcode %}

{% code title=".not_be_empty()" %}
```python
def test_page_has_at_least_one_checkbox(py):
    py.visit('https://the-internet.herokuapp.com/checkboxes')
    assert py.find('[type="checkbox"]').should().not_be_empty()
```
{% endcode %}
