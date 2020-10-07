""" Tests to see what could be faked.

Faker docs: https://faker.readthedocs.io/en/stable/providers.html

* You don't get intellisense
* Use the list of Providers in the above link to know what you can do
* You can use localizations
* You can create your own, custom Providers
"""


def test_fake_name(fake):
    assert fake.name()


def test_fake_first_name(fake):
    assert fake.first_name()


def test_fake_last_name(fake):
    assert fake.last_name()


def test_fake_email(fake):
    assert fake.email()


def test_fake_address(fake):
    assert fake.address()


def test_fake_text(fake):
    assert fake.text()


def test_fake_ssn(fake):
    assert fake.ssn()


def test_fake_locale(fake):
    assert fake.locale()


def test_fake_country(fake):
    assert fake.country()


def test_fake_postal_code(fake):
    assert fake.postalcode()
