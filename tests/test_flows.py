import pytest
from pylenium.driver import Pylenium


@pytest.fixture(scope="session")
def sauce(pys: Pylenium) -> Pylenium:
    """Login to saucedemo.com as standard user."""
    pys.visit("https://www.saucedemo.com/")
    pys.get("#user-name").type("standard_user")
    pys.get("#password").type("secret_sauce")
    pys.get("#login-button").click()
    yield pys
    pys.get("#react-burger-menu-btn").click()
    pys.get("#logout_sidebar_link").should().be_visible().click()


class TestSauceDemo:
    def test_add_to_cart_css(self, sauce: Pylenium):
        """Add an item to the cart. The number badge on the cart icon should increment as expected."""
        sauce.get("[id*='add-to-cart']").click()
        assert sauce.get("a.shopping_cart_link").should().have_text("1")


    def test_add_to_cart_xpath(self, sauce: Pylenium):
        """Add 6 different items to the cart. There should be 6 items in the cart."""
        for button in sauce.findx("//*[contains(@id, 'add-to-cart')]"):
            button.click()
        sauce.getx("//a[@class='shopping_cart_link']").click()
        assert sauce.findx("//*[@class='cart_item']").should().have_length(6)
