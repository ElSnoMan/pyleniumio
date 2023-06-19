---
description: Configure the viewport, or browser window dimensions, for all tests.
---

# 🖥 Viewport

## The Viewport Settings

Let's take a look at the default viewport settings inside of <mark style="color:orange;">**pylenium.json**</mark>

```javascript
"viewport": {
    "maximize": true,
    "width": 1440,
    "height": 900,
    "orientation": "portrait"
}
```

By default, Pylenium will open each browser window in "maximized mode", meaning that the browser window will take up the entire screen that it's running on.

{% hint style="info" %}
With <mark style="color:purple;">`"maximize": true`</mark>, Pylenium ignores the <mark style="color:yellow;">`width`</mark>, <mark style="color:yellow;">`height`</mark>, and <mark style="color:yellow;">`orientation`</mark> values
{% endhint %}

### maximize

* <mark style="color:purple;">`true`</mark> (default) - The browser window will take up the entire screen
* <mark style="color:purple;">`false`</mark> - Use the <mark style="color:yellow;">`width`</mark>, <mark style="color:yellow;">`height`</mark>, and <mark style="color:yellow;">`orientation`</mark> values to set the brower window dimensions

### width & height

These are useful if you want all tests to use the same dimensions instead of dynamically changing to the current screen. For example, running tests locally will probably be different than when running them in your Continuous Integration pipeline.

{% hint style="success" %}
Another useful scenario is for testing your website on different mobile device sizes!
{% endhint %}

{% hint style="info" %}
Make sure <mark style="color:purple;">maximize</mark> is set to <mark style="color:yellow;">`false`</mark>
{% endhint %}

### orientation

* <mark style="color:purple;">`"portrait"`</mark> (default)
* <mark style="color:purple;">`"landscape"`</mark>
