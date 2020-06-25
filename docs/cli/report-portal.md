---
description: CLI commands to easily setup and teardown your RP instance.
---

# Report Portal

{% hint style="success" %}
Make sure to execute these commands in your Project Root.
{% endhint %}

## portal download

Download the default `docker-compose.yml` file needed to spin up the RP instance.

{% hint style="info" %}
This will place the file at your Project Root as `docker-compose.report-portal.yml`
{% endhint %}

{% code title="Terminal $" %}
```text
pylenium portal download
```
{% endcode %}

## portal up

Spin up the RP instance using the downloaded YAML file.

{% code title="Terminal $" %}
```text
pylenium portal up
```
{% endcode %}

You can then open [http://localhost:8080](http://localhost:8080) to see your newly created instance!

## portal down

Teardown the RP instance.

{% hint style="warning" %}
This may or may not work depending on your Terminal on Windows.
{% endhint %}

{% code title="Terminal $" %}
```text
pylenium portal down
```
{% endcode %}

