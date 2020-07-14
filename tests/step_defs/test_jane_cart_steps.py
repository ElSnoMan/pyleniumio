import pytest
from pydantic.main import BaseModel
from pytest_bdd import scenarios, when, parsers, given, then

scenarios('../feature/jane.shopping_bag.feature')

SHOPPING_BAG_ICON = '[data-testid="cart-menu"]'
DEAL_TITLE = '[data-testid="dd-title"]'
DEAL_PRICE = '[data-testid="dd-price"]'
DEAL_SHIPPING = '[data-testid="dd-price-shipping"]'
DEAL_QTY = '[data-testid="dd-qty"]'
ADD_TO_BAG_BUTTON = '[data-testid="add-to-bag"]'

CART_DEAL_TITLE = '[data-testid="product-title"]'
CART_DEAL_SHIPPING = '[data-testid="item-shipping"]'
CART_ITEM_PRICE = '[data-testid="item-price"]'


class Deal(BaseModel):
    name: str
    price: str
    shipping: str
    quantity: str


@given("I am on the Jane Home Page")
def visit_jane(py):
    return py.visit('https://jane.com')


def gather_deal(py) -> Deal:
    shipping_text = py.get(DEAL_SHIPPING).text()
    shipping = '$0.00' if 'FREE' in shipping_text else shipping_text
    return Deal(
        name=py.get(DEAL_TITLE).text(),
        price=py.get(DEAL_PRICE).text(),
        shipping=shipping,
        quantity=py.get(DEAL_QTY).get_attribute('value')
    )


def add_default_item_to_cart(py, quantity) -> Deal:
    py.get('[data-testid="deal-image"]').click()
    for dropdown in py.find('select'):
        dropdown.select(1)
    py.get(DEAL_QTY).clear().type(quantity)
    deal = gather_deal(py)
    py.get(ADD_TO_BAG_BUTTON).click()
    return deal


@given(parsers.cfparse("I add {quantity} item to my cart"))
def i_add_items_to_cart(py, quantity):
    deal = add_default_item_to_cart(py, quantity)
    if not py.title().endswith('/checkout'):
        py.get(SHOPPING_BAG_ICON).click()
    return deal


@when(parsers.cfparse("I add {quantity} item to my cart"))
def when_i_add_items_to_cart(py, quantity):
    deal = add_default_item_to_cart(py, quantity)
    if not py.title().endswith('/checkout'):
        # py.get(SHOPPING_BAG_ICON).click(force=True)
        py.visit('https://jane.com/checkout')
    return deal


@then(parsers.cfparse("I should see the Shopping Bag Icon go up by {quantity}"))
def shopping_bag_icon_goes_up(py, quantity):
    number_of_items = py.get('[data-testid="notification-dot"]').text()
    assert number_of_items == quantity


@then("I should see the item in the cart")
def i_should_see_item_in_the_cart(py, i_add_items_to_cart):
    deal = i_add_items_to_cart
    assert deal.name in py.get(CART_DEAL_TITLE).text()
    assert '1' in py.contains('Quantity').text()
    assert deal.shipping in py.get(CART_DEAL_SHIPPING).text()
    assert deal.price in py.get(CART_ITEM_PRICE).text()


@when("I delete {quantity} item from the cart")
def step_impl():
    raise NotImplementedError(u'STEP: When I delete 1 item from the cart')