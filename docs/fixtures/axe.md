---
description: Accessibility (A11y) Testing with aXe
---

# axe

## Usage

The `axe` fixture is the recommended way to run A11y audits since it's so easy and straightforward.

```python
def test_axe_fixture(py, axe):
    py.visit('https://qap.dev')
    # save the axe report as a file
    report = axe.run(name='a11y_audit.json')
    # and/or use the report directly in the test(s)
    assert len(report.violations) == 0
```

{% hint style="success" %}
 You can generate the report as a JSON and/or use the`AxeReport` object directly.
{% endhint %}

{% hint style="warning" %}
Running an audit will generate a JSON report _only_ if a `name` is given.
{% endhint %}

{% code title="function signature" %}
```python
def run(name: str = None, context: Dict = None, options: Dict = None) -> AxeReport
```
{% endcode %}

## Arguments

* `name: str` The file path \(including name and `.json` extension\) of the report to save as a JSON
* `context: Dict` The dictionary of page part\(s\), by CSS Selectors, to include or exclude in the audit
* `options: Dict` The dictionary of aXe options to include in the audit

{% hint style="info" %}
Visit the official aXe documentation for more information about the `context` and `options` arguments.

[https://github.com/dequelabs/axe-core/blob/master/doc/API.md\#parameters-axerun](https://github.com/dequelabs/axe-core/blob/master/doc/API.md#parameters-axerun)
{% endhint %}

## Yields

* `AxeReport` object that represents the audit report in code

If you include the `name` argument, then that report is also created at the specified file path.

{% hint style="danger" %}
If any of the directories in the path do not exist, then a `FileNotFound` error is raised.
{% endhint %}

