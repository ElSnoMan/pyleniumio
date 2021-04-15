---
description: Summary of notable changes and fixes.
---

# Changelog

## 1.12.3 - 2021-14-04

### Overview

`.select()` and `.select_many()` worked pretty well as expected. However, they wouldn't fail as expected! Because we were trying to combine all the "select strategies" in a single function, it made it harder to test and debug _and_ hid some exceptions... like when an `<option>` didn't exist... whoops!

Now, each strategy has been pulled out into its own method and positive and negative tests have been added to make sure it works 😉

* `.select_by_index(index: int)`
* `.select_by_text(text: str)`
* `.select_by_value(value)`

### Changes

* New `.select_by_*()` methods exist on the `Element` object. Just remember that the dropdowns have to be a `<select>` element!
* `.select()` and `.select_many()` still exist, but show a `DEPRECATED` warning. We will be removing them in a future release
* Our docs have a new home! We are still using GitBook, but we now have the official `docs.pylenium.io` domain! Check it out 😄

## 1.12.2 - 2021-28-01

### Overview

Microsoft's Edge Browser can be used on Macs now, but we hadn't tested it locally on a Mac before. One of our amazing users did and they found a bug! This should now be fixed 😄

### Fixes

Removed `options` from `webdriver_factory.build_edge()` since it isn't needed and was causing the `MicrosoftEdgeDriver` to raise an error.

### Contributors

For anyone looking to contribute, we have changed using `pipenv` as our package manager to `poetry`.

* You can find out more about `poetry` by visiting their website: [https://python-poetry.org](https://python-poetry.org)
* You can see how to setup your machine for Python Development with `poetry` with my [Video on YouTube](https://youtu.be/547Jr26duHQ)

## 1.11.0 - 2020-10-30

### Overview

Pylenium can now do Accessibility \(a11y\) Testing and Audits using aXe! Easily generate JSON reports to share and export or write assertions against it directly in your tests.

### Added

#### aXe integration

There are two ways to start using aXe in your tests:

* `PyleniumAxe` class from `pylenium.a11y` module
* `axe` fixture \(recommended\)

```python
def test_axe_fixture(py, axe):
    py.visit('https://qap.dev')
    # save the axe report as a file
    report = axe.run(name='a11y_audit.json')
    # and/or use the report directly in the test(s)
    assert len(report.violations) == 0
```

In the above example, we are using Pylenium to navigate to the website and then `axe` to run the audit, generate the report, and check that we have zero violations!

#### iframes

The main change here is the ability to drag and drop within iframes. Pylenium uses jQuery to perform this action, but we need to inject jQuery if the page doesn't already have it. However, in V1 of our jQuery implementation, it would only inject into the main document and not within each iframe. This is now fixed!

* Pylenium's jQuery V2 now comes in its own module and injects into all iframes of the page
* `py.switch_to` now comes with a `py.switch_to.frame_by_element()` which is useful when the iframe does not have an `id` or `name` attribute

```python
iframe = py.get('iframe')
py.switch_to.frame_by_element(iframe)
```

## 1.10.0 - 2020-10-7

### Overview

Pylenium can now gather Web Performance metrics right from the browser and into your hands! Through Pylenium's Performance API, you can leverage the different Performance and Timing objects that each browser tracks and generates. Also, we have created some custom data points, like `Time to Interactive`, `Page Load Time`, and `Time to First Contentful Paint`!

### Added

* Performance API

```python
# Access the Performance API right from py
perf = py.performance.get()
```

* WindowPerformance Object

The main abstraction that holds all of these metrics and data points.

```python
# get the TTI
tti = py.performance.get().time_to_interactive()
```

* Stopwatch Decorator

The `performance.py` module includes a Stopwatch Decorator that you add to any function. This will log how long it takes for that function to complete!

```python
# 1. How long does it take to add an item to the cart?
@stopwatch
def add_item_to_cart(py):
    py.get('#add-item').click()
    py.get('#added-notification').should().be_visible()

# 2. How long does it take to edit an item's available stock via the API and see it change in the UI?
@stopwatch
def update_available_stock(py, item, quantity):
    payload = {'item': item, 'qty': quantity}
    api.items.update(payload)
    py.get(f'#available-stock-{item}').should().have_text(quantity)
```

* CONTRIBUTING.md
* CODE\_OF\_CONDUCT.md

#### Linked Issues

[Gather Web Performance data and log how long actions take](https://app.gitkraken.com/glo/view/card/c08c640de7754a2f9cd68034ffbd93a4)

## 1.9.7 - 2020-09-28

### Added

* Github Actions CI to Pylenium repo
* Pylenium CLI: `pylenium version` is now `pylenium --version`

If you want to import the `Pylenium` class into a Module, you used to do this:

```python
from pylenium import Pylenium
```

This has now been changed \(for CI reasons\) to:

```python
from pylenium.driver import Pylenium
```

So make sure you update this import statement if you were using the previous version!

### Fixes

* pytest version 6.1.0 \(released in September 2020\) causes issues within Pylenium's conftest.py. Changed Pipfile to use previous version until a solution is found
* `is_checked()` now works for Radio Buttons and Checkboxes

## 1.9.0 - 2020-06-24

> Changes were made to the `conftest.py` file, so make sure to run `pylenium init -c` after upgrading to `1.9.0` to overwrite it with the latest. Not doing this will likely result in `ModuleNotFoundErrors`

### Report Portal \(RP\)

RP is now natively supported by Pylenium! If you are not already familiar with Report Portal, I highly suggest you check it out. It gives you robust reporting and categorizing of your test runs and results and is backed with machine learning! [https://reportportal.io](https://reportportal.io)

We had very basic logging and reporting, but we wanted to provide a better and more robust reporting solution. After a lot of research, we landed on RP. They are not only free and Open Source, but they also have a great community, Slack group, and YouTube channel with different demos and presentations to help you take your reporting to the next level. This level of modern support was crucial in our decision and we hope you enjoy it!

### **Added**

* `pylenium init` now also creates a default `pytest.ini` file at your Project Root. This contains values to easily connect with RP.
* `pylenium portal` [CLI Commands](cli/report-portal.md) to quickly setup your RP instance

```bash
# 1. Download the docker-compose file used to spin up RP
pylenium portal download

# 2. Configure your machine and this docker-compose.yml based on your OS and needs
#     by going to https://reportportal.io/docs/Deploy-with-Docker
```

```bash
# 3. Spin up the RP instance
pylenium portal up
```

That's it! You'll get helpful hints as you execute each command so you know where to go and how to login. Happy reporting!

### **Fixes**

* `get_xpath` and `find_xpath` functions were not behaving as expected. This has been fixed, but we have also renamed them to
  * `getx()`
  * `findx()`
* `AttributeError` was raised if there were more than one `pytest_runtest_makereport` fixtures in the project.
* Logging now uses the built-in `logging` python package, but screenshots are still saved to the `test_results` directory.

## 1.8.2 - 2020-05-21

### Changed

* **`Element.should().not_exist()` --&gt; `Element.should().disappear()`**

If the intent is to check that the element is not on the page, then use:

```python
py.should().not_find()
```

If the intent is to wait until an existing element does not exist anymore or "disappear", then you used to have to do

```python
py.get().should().not_exist()
```

However, this is clearly confusing because the way `should not exist` reads would suggest that both options are the same. This has now been changed to more clearly reflect that intent.

```python
py.get().should().disappear()
```

* **`Element.should().have_attr()` doesn't require the `value` argument**

There is a scenario when all you want to check on an element is that an attribute exists or not.

Example:

```python
py.wait().until(lambda _: toggle.get_attribute('aria-checked'))
```

Unfortunately, `ElementShould.have_attr()` requires an attribute name AND a value. Trying to use it in this scenario is difficult to use or straight up doesn't work.

```python
# doesn't work
py.get(TOGGLE).should().have_attr('aria-checked', True)

# doesn't work either
py.get(TOGGLE).should().have_attr('aria-checked', '')

# this is just confusing...
py.get(TOGGLE).should().not_have_attr('aria-checked', None)

# this may work if it sees the custom `aria-checked` attribute as "checked"
py.get(TOGGLE).should().be_checked()
```

### **Solution**

Make the existing expectations not require the `value` argument.

* `should().have_attr(name, value=None)`
* `should().not_have_attr(name, value=None)`

### Fixed

* `drag_and_drop.js` was not included in the pylenium installation. Now it is!
* Some typos

## 1.8.0 - 2020-05-11

### Added

This is a bigger change that sets us up for things we want to do with better reporting and BDD functionality. There may be some breaking changes depending how you wrote your tests.

For example, the property of `Element.text` is now a function `Element.text()` and `.find()` no longer has an `at_least_one` parameter.

Make sure you run your tests after upgrading to catch errors like `str is not invocable`. They should be easy to fix.

### **PyleniumShould**

The use case of checking that an element is NOT on the page or DOM was much more common than anticipated. I have changed how the `.find()` and `.find_xpath()` functions behave to help with this, but there are now three easy to use "should" commands as well.

* **`.not_find()`**
* **`.not_find_xpath()`**
* **`.not_contain()`**

```python
# example usage
py.should().not_find('#hidden-element')
```

### **Driver**

Having these as properties was actually messing people up as they used Pylenium. Because almost all of the commands are functions, it was common that someone would try `py.url()` or `py.title()` only to see the test fail saying that `str is not invocable`. Changing these to functions feels more natural.

* `.url` property changed to `.url()` function
* `.title` property changed to `.title()` function

### **XPaths**

Removed the `.xpath()` function from _Pylenium_ and _Element_ and replaced with `get` and `find` options. The `.xpath()` function _could_ return an empty list, a single element, or a list of 2 or more elements. The flexibility was pretty "clever", but it was not intuitive to work with. Separating it into two distinct functions to match the CSS versions of `get()` and `.find()` made more sense.

* `.get_xpath()`
* `find_xpath()`

```python
# single element with xpath
py.get_xpath('//input[@name="q"]')

# list of elements with xpath
py.find_xpath('//li')
```

### **Find Elements**

The `.find()` and `.find_xpath()` functions on the _Pylenium_ and _Element_ objects will now return an empty list if none are found rather than throwing an exception. Dealing with an empty list is easier and cleaner than having to handle an exception.

However, this is not the case If the timeout is set to `0` \(zero\). The next section goes into more detail.

### **Immediate Poll with timeout=0**

There are times when you don't want to use an awesome wait and a timeout of 1 second isn't good enough. For all of the _Find Element_ commands, you can now set the timeout to `0` \(zero\) to poll the DOM immediately as if you were using Selenium with no wait.

> This will still return an `Element` or `Elements` object if found, but no _wait_ is used.

Let's take a look at the `.get()` signature:

```python
def get(self, css: str, timeout: int = None) -> Element
```

* If `timeout=None` \(default\), the function will use the default `wait_time` in `pylenium.json` which is 10 seconds.

```python
# use `wait_time` in pylenium.json
py.get('#button').click()
```

* If `timeout > 0`, override the default wait\_time.

```python
# shorten it to 3 seconds instead
py.get('#button', timeout=3).click()

---or---

# give it even more time
py.get('#button', timeout=30).click()
```

* If timeout=0, poll the DOM immediately without any waiting.

```python
# no waiting, immediately poll the DOM
py.get('#button', timeout=0).click()
```

### **Element and Elements**

Changed some properties to functions for the same reasons as the props in Driver.

* `Elements.length` property changed to `Elements.length()` function
* `Element.tag_name` property changed to `Element.tag_name()` function
* `Element.text` property changed to `Element.text()` function

### **ElementsShould**

_Pylenium_ and _Element_ have their own Should classes for expectations. Most of our assertions and checks are done against them, but there were enough use cases against the length of the Elements that I wanted to include them to make it easier. Now when you have a list of elements \(Elements\), you can use `.should()`:

* `be_empty()`
* `not_be_empty()`
* `have_length()`
* `be_greater_than()`
* `be_less_than()`

## 1.7.7 - 2020-05-08

### Added

Pylenium CLI

### Details

After a fresh install of pyleniumio, you now need to initialize pylenium using the Pylenium CLI:

```bash
$ pylenium init
```

You can also see the available options using the `--help` argument.

```bash
$ pylenium init --help
```

This will create the `conftest.py` file needed by Pylenium as well as the default `pylenium.json` config file.

{% hint style="info" %}
Run this command at the Project Root so Pylenium is globally accessible by all files/tests in your project.
{% endhint %}

### Purpose

Originally, Pylenium would copy a conftest.py file and overwrite any existing conftest.py files the user had at the Project Root. This was a necessary side effect with how `setup.py` was working. With `pylenium init`, you now have the option to create or overwrite these files rather than needing to start from scratch.

`pylenium init` also creates a default `pylenium.json` so the user knows what config values they can change globally. This makes for a much easier experience for users.

This also removes the requirement of the user being in the context of a virtual environment. Although this is still 100% recommended, `pylenium init` can be executed in or out of the venv.

## 1.6.2 - 2020-05-07

### Added

* `options.add_extension()`
* `Element.open_shadow_dom()`

### Details

**Add Extension**

You can now easily add extensions to your browser sessions by either using the `--extensions` CLI argument and passing in a list of file paths, or you can also do this in the `pylenium.json`

```javascript
{
    "driver": {
        "extension_paths": ["path.crx", "other-path.crx"]
    }
}
```

**Shadow DOM**

Shadow DOMs are a bit tricky, but you can now find elements within them by using the `Element.open_shadow_dom()` command. Check out this example using `chrome://extensions`:

```python
def test_loading_extension_to_browser(py):
    py.visit('chrome://extensions/')
    shadow1 = py.get('extensions-manager').open_shadow_dom()
    shadow2 = shadow1.get('extensions-item-list').open_shadow_dom()
    extension_shadow_dom = shadow2.find('extensions-item')[1].open_shadow_dom()
    assert extension_shadow_dom.get('#name-and-version').should().contain_text('Get CRX')
```

## 1.6.1 - 2020-05-01

### Added

* `drag_to( css )`
* `drag_to_element( to_element )`

### Details

`Element.drag_to( css )` will drag the current element to the element with the given CSS.

```python
py.get('#draggable-box').drag_to('#drop-here')
```

`Element.drag_to_element( to_element )` will drag the current element to the given element.

```python
to_element = py.get('#drop-here')
py.get('#draggable-box').drag_to(to_element)
```

```python
# one more example
from_element = py.get('#draggable-box')
to_element = py.get('#drop-here')

from_element.drag_to_element(to_element)
```

## 1.6.0 - 2020-04-28

### Added

* Page Load Wait Time
* Test Case Name into Capabilities for frameworks like Selenoid
* Add Experimental Options via `pylenium.json`

### Details

**Page Load Wait Time**

By default, the Page Load timeout is `0` just like Selenium. However, there were cases where users wanted to control this globally or as needed per test case. You can now do this a few different ways:

```bash
# set it globally in CLI
--page_load_wait_time 10
```

```javascript
// set it globally in pylenium.json
{
    "page_load_wait_time": 10
}
```

```python
# override the global page_load_wait_time just for the current test
py.set_page_load_timeout(10)
```

**Test Case Name into Capabilities**

This was primarily for other frameworks like Selenoid and Zalenium that used this name to label the tests in their runners. For example, in Selenoid, you can filter tests by name. Before this change, the tests were given an unhelpful, generic name instead of the proper test name. That's fixed now :\)

**Add Experimental Options**

For users that want to use some of the experimental options for browsers, you can now do this within `pylenium.json`. This is a list of dictionaries \(key-value pairs\) that you want to include globally.

```javascript
{
    "experimental_options": [
        {"useAutomationExtension": false},
        {"otherName": "value"}
    ]
}
```

## 1.5.4 - 2020-04-27

### Added

* `WebDriverFactory().build_capabilities()`
* capabilities is a single dictionary instead of a list of dictionaries

Originally I wasn't going to add capabilities because it was going to be deprecated in Selenium 4. However, it seems enough people need it \(including my very own Workfront\) and even with Selenium 4, there will be cases where they are needed.

Also, with the refactor it became very clear that a single dictionary of capabilities was much better than a list of them. This change has been reflected in `pylenium.json` as well as in the CLI args.

{% code title="pylenium.json" %}
```python
{
    "driver": {
        "capabilities": {
            "enableVNC": true,
            "enableVideo": false,
            "name": "value"
        }
    }
}
```
{% endcode %}

{% code title="Terminal" %}
```python
--caps = '{"name": "value", "boolean": true}'
```
{% endcode %}

## 1.5.2 - 2020-04-24

### Added

* `EdgeChromiumDriver`
* `Customize DesiredCapabilities`

### Details

* `EdgeChromiumDriver`

{% code title="pylenium.json" %}
```python
{
    "driver": {
        "browser": "edge"
    }
}
```
{% endcode %}

{% code title="Terminal" %}
```python
--browser="chrome"
```
{% endcode %}

* `Customize DesiredCapabilities`

```javascript
// pylenium.json

{
  "driver": {
    "capabilities": [
        {"name": "value"}
    ]
  }
}
```

{% code title="Terminal" %}
```python
--caps [{"name1": "value1"}, {"name2": "value2"}]
```
{% endcode %}

## 1.4.1 - 2020-04-17

### Added

* `webdriver_manager`
* `configure pylenium.json`

### Details

* `webdriver_manager`

This is the biggest change made in this release. Pylenium now uses `webdriver_manager` to install the necessary driver binaries to the user's machine automatically!

> This means that the user does NOT need to worry about installing them anymore!

Of course, they will still need the actual browser installed, but that's much easier than installing the driver binaries and adding them to the PATH.

This is a great step in making UI Automation with Pylenium a pleasant experience for everyone :\)

* `pylenium.json defaults`

Prior to this release, we would install a `pylenium.json` file at the Project Root alongside our conftest.py. The issue is that this JSON file was meant to be an easy way to control Pylenium's settings \(which it was\), but is overriden every time they would update to a new version of Pylenium...

This also caused issues in CI/CD pipelines because they could not rely on this file to configure Pylenium since installing it fresh in the pipeline would give you a fresh pylenium.json...

This is now taken care of! We are using our BaseModel classes to use defaults that can be overriden two different ways:

1. They can still override them using the CLI options. For example:  `pytest tests --browser='opera'`
2. They can create a `pylenium.json` at the Project Root \(same dir as conftest.py\) with the values they want to override. They can also include any other key/value pairs in the `custom` object:

```javascript
// pylenium.json

{
    driver: {
        "wait_time": 5
    }
    custom = {
        "foo": "bar"
    }
}
```

```python
# use it in code
py.config.custom.get('foo')  # => yields "bar"

---or---

py.config.custom['foo']  # => yields "bar"
```

## 1.3.0 - 2020-04-05

### Fixed

* Updated the tests in the examples directory
* Fixed an issue when using `PyleniumWait`

### Added

* `py.should()` - A collection of expectations for the current driver \( [\#15](https://github.com/ElSnoMan/pyleniumio/issues/15) \)
* `Element.should()` - A collection of expectations for the current element \( [\#36](https://github.com/ElSnoMan/pyleniumio/issues/36) \)
* `Element.get_property()`
* `Element.is_enabled()`
* `Elements.is_empty()`

## 1.2.10 - 2020-03-24

### Added

* `Element.select(value)` - value can now be the index of the option

## 1.2.9 - 2020-03-23

### Added

* `py.scroll_to(x, y)` - Scroll x and y pixels on the page
* `Element.scroll_into_view()` - Scroll the element into the viewport
* `Element.right_click()` - Right click on the element

## 1.2.8 - 2020-03-21

### Fixed

* `DesiredCapabilities` error if user had an old version of chromedriver
* `py.switch_to.frame()` wasn't switching to frame properly

### Added

* **`PyleniumWait`**
* **Pylenium Commands &gt; wait** -  doc with Usage examples

### Changed

* Custom timeouts to some commands, like `.get()`, to override global wait\_time in pylenium.json

## 1.2.7 - 2020-03-17

### Added

* Official release of V1 to the Autobots class
* The core functionality of Pylenium

