---
description: A collection of expected conditions against an Element.
---

# ⏱ Element.should()

## Expectations

### Positive Conditions

* <mark style="color:purple;">`.be_checked()`</mark>
* <mark style="color:purple;">`.be_clickable()`</mark>
* <mark style="color:purple;">`.be_disabled()`</mark>
* <mark style="color:purple;">`.be_enabled()`</mark>
* <mark style="color:purple;">`.be_focused()`</mark>
* <mark style="color:purple;">`.be_hidden()`</mark>
* <mark style="color:purple;">`.be_selected()`</mark>
* <mark style="color:purple;">`.be_visible()`</mark>
* <mark style="color:purple;">`.contain_text(text: str, case_sensitive=True)`</mark>
* <mark style="color:purple;">`.disappear()`</mark>
* <mark style="color:purple;">`.have_attr(attr: str, value: Optional[str])`</mark>
* <mark style="color:purple;">`.have_class(class_name: str)`</mark>
* <mark style="color:purple;">`.have_prop(prop: str, value: str)`</mark>
* <mark style="color:purple;">`.have_text(text: str, case_sensitive=True)`</mark>
* <mark style="color:purple;">`.have_value(value: any)`</mark>

### Negative Conditions

* <mark style="color:purple;">`.not_be_focused()`</mark>
* <mark style="color:purple;">`.not_have_attr(attr: str, value: Optional[str])`</mark>
* <mark style="color:purple;">`.not_have_text(text: str, case_sensitive=True)`</mark>
* <mark style="color:purple;">`.not_have_value(value: any)`</mark>



## Syntax

```python
# Use the default wait_time
Element.should().<expectation>

---or---

# Customize the wait_time for this expectation
Element.should(timeout: int).<expectation>

---or---

# Ignore exceptions that you expect to "get in the way"
Element.should(ignored_exceptions: list).<expectation>

---or---

# Customize both fully
Element.should(timeout: int, ignored_exceptions: list).<expectation>
```

## Examples

{% code title="Is element displayed?" %}
```python
def test_element_visible(py):
    py.visit("https://qap.dev")
    assert py.get("a[href='/about']").should().be_visible()
```
{% endcode %}

{% code title="Does it have text?" %}
```python
def test_element_has_correct_text(py):
    py.visit("https://qap.dev")
    assert py.get("a[href='/about']").should().have_text("About")
```
{% endcode %}

## Yields

* <mark style="color:orange;">**Element**</mark> - If the assertion passes, then the current Element is returned, else an **AssertionError** is raised if the condition is not met within the specified timeout.
