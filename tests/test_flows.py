import pytest
from pylenium.driver import Pylenium


@pytest.fixture
def sauce(py: Pylenium) -> Pylenium:
    """Login to saucedemo.com as standard user."""
    py.visit("https://www.saucedemo.com/")
    py.get("#user-name").type("standard_user")
    py.get("#password").type("secret_sauce")
    py.get("#login-button").click()
    yield py
    py.get("#react-burger-menu-btn").click()
    py.get("#logout_sidebar_link").should().be_visible().click()


def test_add_to_cart_css(sauce: Pylenium):
    """Add an item to the cart. The number badge on the cart icon should increment as expected."""
    sauce.get("[id*='add-to-cart']").click()
    assert sauce.get("a.shopping_cart_link").should().have_text("1")


def test_add_to_cart_xpath(sauce: Pylenium):
    """Add 6 different items to the cart. There should be 6 items in the cart."""
    for button in sauce.findx("//*[contains(@id, 'add-to-cart')]"):
        button.click()
    sauce.getx("//a[@class='shopping_cart_link']").click()
    assert sauce.findx("//*[@class='cart_item']").should().have_length(6)
