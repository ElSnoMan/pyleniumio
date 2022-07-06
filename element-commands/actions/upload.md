---
description: The command to upload a file to the element.
---

# upload

## Syntax

```python
Element.upload(filepath: str) -> Element
```

## Usage

{% code title="correct usage" %}
```python
py.get("#file-upload").upload("path/to/file.png")
```
{% endcode %}

{% code title="incorrect usage" %}
```python
# Errors, must be an element that can accept an upload
py.get("a").upload("path/to/file.png")
```
{% endcode %}

## Arguments

* <mark style="color:purple;">**filepath (str)**</mark> - The absolute path to the file including the name and extension

{% hint style="success" %}
You can use Path objects to make this easier and work for any OS
{% endhint %}

## Yields

* <mark style="color:orange;">**Element**</mark> - The element you attempted to upload to

## Examples

Before the `upload()` command, you would do this:

```python
# Selenium .send_keys()
driver.find_element(By.ID("select-file")).send_keys("path/to/file.png")

# Pylenium .type()
py.get("#select-file").type("path/to/file.png")
```

That was not as clear or intuitive :cry:, but now it's much cleaner!

```python
py.get("#select-file").upload("path/to/file.png")
py.get("#upload-button").click()
```

{% hint style="info" %}
Give it a try! [https://the-internet.herokuapp.com/upload](https://the-internet.herokuapp.com/upload)
{% endhint %}
