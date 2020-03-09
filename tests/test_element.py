
def test_element_with_no_siblings(driver):
    elements = driver.get("[href='https://spy.deckshop.pro/']").siblings()
    assert elements.length == 0


def test_element_parent_and_siblings(driver):
    parent = driver.get("a.nav-link[href='https://spy.deckshop.pro/']").parent()
    assert parent.tag_name == 'li'
    assert parent.siblings().length == 8


def test_element_text(driver):
    assert driver.contains('More info').text == 'More info'


def test_find_in_element_context(driver):
    headers = driver.find('h5')
    assert 'Royal Delivery Golem beatdown' in headers[1].get("a").text


def test_input_type_and_get_value(driver):
    search_field = driver.get('#smartSearch')
    assert search_field.type('golem').get_attribute('value') == 'golem'
    assert search_field.clear().get_attribute('value') == ''
