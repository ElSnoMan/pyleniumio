---
description: Commands to find elements within the context of another element.
---

# 🔍 Find Elements

The <mark style="color:orange;">**Element**</mark> class provides 5 main ways to find elements:

* [contains](../driver-commands/find-elements/contains.md)   get a <mark style="color:yellow;">single element</mark> by **TEXT**
* [find](../driver-commands/find-elements/find.md)           find a <mark style="color:yellow;">list of elements</mark> by **CSS**
* [findx](../driver-commands/find-elements/find\_xpath.md)         find a <mark style="color:yellow;">list of elements</mark> by **XPATH**
* [get](../driver-commands/find-elements/get.md)            get a <mark style="color:yellow;">single element</mark> by **CSS**
* [getx](../driver-commands/find-elements/get\_xpath.md)          get a <mark style="color:yellow;">single element</mark> by **XPATH**

These are very similar to how <mark style="color:orange;">**py**</mark> finds elements. For example, the following code snippet will   search the _**entire**_ DOM (aka webpage) for the first Element with <mark style="color:purple;">`id=name`</mark> and type "Carlos Kidman" into it.

```python
py.get("#name").type("Carlos Kidman")
```

Now take a look at the next code snippet:

```python
py.get(".form").get("#city").type("Salt Lake City")
```

This starts by searching the entire DOM for an element with <mark style="color:purple;">`class=form`</mark>. Then, _**within** _ the form element, search for the first element with <mark style="color:purple;">`id=city`</mark> and type "Salt Lake City" into it.

Also, you can hold <mark style="color:orange;">**Element**</mark> and <mark style="color:orange;">**Elements**</mark> in variables instead of chaining them like the snippet above. The ability to set this context with a smaller scope can be powerful!

```python
form = py.get(".form")
form.get("#name").type("Carlos Kidman")
form.get("#city").type("Salt Lake City")
form.get("#search").submit()
```
