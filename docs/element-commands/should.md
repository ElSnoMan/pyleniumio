---
description: A collection of expectations for the current Element or Elements.
---

# should

## Element Expectations \(ElementShould\)

### Positive Conditions

* `.be_checked()`
* `.be_clickable()`
* `.be_disabled()`
* `.be_enabled()`
* `.be_focused()`
* `.be_hidden()`
* `.be_selected()`
* `.be_visible()`
* `.contain_text()`
* `.disappear()`
* `.have_attr()`
* `.have_class()`
* `.have_prop()`
* `.have_text()`
* `.have_value()`

### Negative Conditions

* `.not_be_focused()`
* `.not_have_attr()`
* `.not_have_text()`
* `.not_have_value()`

## Elements Expectations \(ElementsShould\)

### Positive Conditions

* `.be_empty()`
* `.have_length()`
* `.be_greater_than()`
* `.be_less_than()`

### Negative Conditions

* `.not_be_empty()`

## Syntax

```python
# use the default wait_time
Element.should().<expectation>
Elements.should().<expectation>

---or---

# customize the wait_time for this expectation
Element.should(timeout).<expectation>
Elements.should(timeout).<expectation>

---or---

# ignore exceptions that you expect to "get in the way"
Element.should(ignored_exceptions).<expectation>
Elements.should(ignored_exceptions).<expectation>

---or---

# customize both fully
Element.should(timeout, ignored_exceptions).<expectation>
Elements.should(timeout, ignored_exceptions).<expectation>
```

## Usage

{% code title="correct usage" %}
```python
py.get('#about-link').should().have_text('About')

---or---

py.find('li > a').should().have_length(10)
```
{% endcode %}

## Arguments

### No args

* `.be_checked()`
* `.be_clickable()`
* `.be_disabled()`
* `.be_enabled()`
* `.be_focused()`
* `.be_hidden()`
* `.be_selected()`
* `.be_visible()`
* `.disappear()`
* `.not_be_focused()`
* `.be_empty()`
* `.not_be_empty()`

### Have args

* `.contain_text(text)`
* `.have_attr(attribute, value=None)`
* `.have_class(class_name)`
* `.have_prop(property)`
* `.have_text(text, case_sensitive=True)`
* `.have_value(value)`
* `.not_have_attr(attribute)`
* `.not_have_text(text)`
* `.not_have_value(value)`
* `.have_length(int)`
* `.be_greater_than(int)`
* `.be_less_than(int)`

## Yields

* **\(Element\)** If the assertion passes, then the current Element is returned, else an **AssertionError** is raised if the condition is not met within the specified timeout.

