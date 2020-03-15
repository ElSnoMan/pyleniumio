---
description: pytest is a modern and powerful Test Framework
---

# Setup pytest

Install **Pylenium** into your [Virtual Environment](virtual-environments.md) if you haven't already:

```bash
$ (venv) pip install pyleniumio
```

To get the most out of your IDE, you need to configure it to use **pytest** as the Test Framework.

{% tabs %}
{% tab title="VS Code" %}
```
Open Command Palette (CMD + SHIFT + P or CTRL + SHIFT +P)
Search for "Python: Configure Tests"
Select pytest

# VS Code doesn't fully support pytest so you won't get things like IntelliSense
```
{% endtab %}

{% tab title="PyCharm" %}
```
Open Preferences (or Settings)
Open Tools > Python Integrated Tools
Select pytest in the "Default test runner" dropdown
```
{% endtab %}
{% endtabs %}

{% hint style="info" %}
Visit the pytest docs for more info: [https://docs.pytest.org/](https://docs.pytest.org/)
{% endhint %}



