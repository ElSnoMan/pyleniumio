---
description: A collection of expected conditions against an Element.
---

# ⏱ Element.should()

## Expectations

### Positive Conditions

* `.be_checked()`
* `.be_clickable()`
* `.be_disabled()`
* `.be_enabled()`
* `.be_focused()`
* `.be_hidden()`
* `.be_selected()`
* `.be_visible()`
* `.contain_text(text: str, case_sensitive=True)`
* `.disappear()`
* `.have_attr(attr: str, value: Optional[str])`
* `.have_class(class_name: str)`
* `.have_prop(prop: str, value: str)`
* `.have_text(text: str, case_sensitive=True)`
* `.have_value(value: any)`

### Negative Conditions

* `.not_be_focused()`
* `.not_have_attr(attr: str, value: Optional[str])`
* `.not_have_text(text: str, case_sensitive=True)`
* `.not_have_value(value: any)`



## Syntax

```python
# use the default wait_time
Element.should().<expectation>

---or---

# customize the wait_time for this expectation
Element.should(timeout: int).<expectation>

---or---

# ignore exceptions that you expect to "get in the way"
Element.should(ignored_exceptions: list).<expectation>

---or---

# customize both fully
Element.should(timeout: int, ignored_exceptions: list).<expectation>
```

## Examples

{% code title="Is element displayed?" %}
```python
def test_element_visible(py):
    py.visit('https://qap.dev')
    assert py.get('a[href="/about"]').should().be_visible()
```
{% endcode %}

{% code title="Does it have text?" %}
```python
def test_element_has_correct_text(py):
    py.visit('https://qap.dev')
    assert py.get('a[href="/about"]').should().have_text('About')
```
{% endcode %}

## Yields

* **(Element)** If the assertion passes, then the current Element is returned, else an **AssertionError** is raised if the condition is not met within the specified timeout.
