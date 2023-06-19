---
description: A basic instance of Faker to generate test data.
---

# fake

{% hint style="success" %}
Read the [Official Faker Docs](https://faker.readthedocs.io/en/stable/providers.html) for more info! There's a lot you can do with it.
{% endhint %}

## Syntax

```
py.fake.<object>()
```

{% hint style="info" %}
This is a **command** and a **fixture**. More details in his doc: [**Fixtures > fake**](../docs/fixtures/fake.md)
{% endhint %}

## Examples

```python
# Generate fake names
py.fake.name()
py.fake.first_name()
py.fake.last_name()

# Generate a bunch of other things!
py.fake.email()
py.fake.address()
py.fake.ssn()
```



