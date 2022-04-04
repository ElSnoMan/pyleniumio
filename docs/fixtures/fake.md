---
description: A basic instance of Faker to generate test data.
---

# fake

## What is Faker?

Put simply, Faker is a library that generates fake data for you.

{% hint style="info" %}
Check out their docs when you have some time: [https://faker.readthedocs.io](https://faker.readthedocs.io/en/stable/index.html)
{% endhint %}

## Three Ways to Use it

* `py.fake` - A basic Faker instance for UI tests
* `fake fixture` - A fixture of Faker for any tests
* `Create your own` - Some users may need advanced functionality like **Locales** and **Providers**

{% hint style="info" %}
This doc will go over the first two. Check out their docs for more advanced usage.
{% endhint %}

## Syntax

```python
# Faker instance for UI tests
py.fake

---or---

# fake fixture to be used in any tests
def test_(fake)
```

## Usage

{% code title="py.fake" %}
```python
def test_new_user_flow(py):
    py.visit('https://some-page.com')
    py.get('#email').type(py.fake.email())
    py.get('#password').type(py.fake.password())
    py.contains('Login').click()
    assert py.contains('Success!')
```
{% endcode %}

{% code title="fake fixture" %}
```python
def test_fake_cc_expire(fake):
    fake.credit_card_expire(start='now', end='+10y', date_format='%m/%y')
    # '07/27'
    

def test_fake_address(fake):
    fake.address()
    # '00232 Isabel Creek\nReynoldsport, CA 05875'
```
{% endcode %}

## What can I fake?

To see a full list of all the default providers that come out of the box, go to the link below:

{% embed url="https://faker.readthedocs.io/en/stable/providers.html" %}

## FAQs

When I type `py.fake.`, I'm not seeing `address()` or anything else in your examples. What gives?

* Because of the way Faker works with their Providers, you don't get IntelliSense. This is good and bad. Bad because you don't see all the options that are available, but good because you can create your own, custom Providers to generate almost everything you'd need for your applications and systems. Just type `py.fake.address()` and it will work!

Which of the three approaches should I use?

* It's entirely up to you and your needs and style. This is completely valid:

```python
def test_a_page(py, fake):
    py.visit('https://page.').get('#email').type(fake.email())
```

* If you need more advanced power, you can always create your own instance of Faker:

```python
from faker import Faker

fake = Faker()
```
