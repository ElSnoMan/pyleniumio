---
description: Connect your tests to a RP instance.
---

# Report Portal

{% hint style="info" %}
This doc assumes you are already familiar with the [Report Portal CLI commands](../cli/report-portal.md)
{% endhint %}

## Configure with pytest.ini

Once you've spun up your instance of Report Portal (RP), there are only a few values you need to change in the `pytest.ini` file created when you ran `pylenium init`.

Here is the default pytest.ini file:

```graphql
[pytest]
;ReportPortal `pytest-reportportal` plugin
;ReportPortal (required)
rp_endpoint = http://localhost:8080
rp_uuid = [UUID from USER PROFILE section of ReportPortal]
rp_launch = EXAMPLE_TEST_RUN_NAME
rp_project = default_personal

;For more info, including other pytest.ini options, visit: https://github.com/reportportal/agent-python-pytest
;ReportPortal (optional)
rp_ignore_errors = True
rp_hierarchy_dirs = True
rp_hierarchy_module = False
rp_hierarchy_class = False
```

{% hint style="info" %}
The only value that _needs ****_ be changed is the `rp_uuid` which is the **ACCESS TOKEN** to connect
{% endhint %}

### Launch and Project

* `rp_launch` is the name of the **Test Run** and is the grouping of tests that will be reported to RP under the **Launches** tab.
* `rp_project` is the name of the **Project** that you would like the Launch to report to.

By default, there is a `superadmin_personal` and a `default_personal` project when you first spin up your instance of RP. You can switch between them or create more on the **Administrate** page under the User Menu.

{% hint style="info" %}
Any of these variables _can_ be overridden via the CLI in case you need them defined at runtime.
{% endhint %}

### Get the ACCESS TOKEN

Once you have logged in to your instance of RP, go to the **Profile** page under the User Menu in the top right corner. This will have the ACCESS TOKEN for you to copy.

Paste this into the `rp_uuid` value in `pytest.ini` and save. That's it!

## Run the Tests

All that's left is to run the tests like usual, but now include the `--reportportal` flag.

{% code title="Example" %}
```bash
pytest tests/test_checkout.py --reportportal
```
{% endcode %}

Refresh the Launches tab and you should now see your Test Run!

{% hint style="success" %}
There's a lot you can do, so make sure to visit their docs for more: [https://reportportal.io/docs](https://reportportal.io/docs)
{% endhint %}
