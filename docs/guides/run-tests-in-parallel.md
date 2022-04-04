# Run Tests in Parallel

## Simple CLI

Pylenium comes with **pytest** and the **pyest-xdist** plugin to run tests concurrently. All you need to do is use the `-n [NUMBER]` option when running the tests in the CLI.

{% code title="Terminal $ (venv) # run 2 tests concurrently" %}
```bash
python -m pytest tests -n 2
```
{% endcode %}

{% hint style="success" %}
&#x20;Pylenium is already designed to scale in parallel with or without containers
{% endhint %}

## Configure the IDE

Most IDEs will allow you to configure your Test File or Test Run with additional arguments.

For example, in PyCharm, you can:

* Open **Run** in the Top Menu
* Select **Edit Configurations**
* Then add `-n 2` to the **Additional Arguments** field

{% hint style="info" %}
That allows you to Run and Debug tests while still having 2 run at a time
{% endhint %}

