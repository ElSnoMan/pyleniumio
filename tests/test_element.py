
def test_element_with_no_siblings(py):
    py.visit('https://deckshop.pro')
    elements = py.get("a[href='/spy/']").siblings()
    assert elements.length == 0


def test_element_parent_and_siblings(py):
    py.visit('https://deckshop.pro')
    parent = py.get("a.nav-link[href='/spy/']").parent()
    assert parent.tag_name == 'li'
    assert parent.siblings().length == 8


def test_element_text(py):
    py.visit('https://deckshop.pro')
    assert py.contains('More info').text == 'More info'


def test_find_in_element_context(py):
    py.visit('https://deckshop.pro')
    headers = py.find('h5')
    assert 'Mega Knight' in headers[1].get("a").text


def test_input_type_and_get_value(py):
    py.visit('https://deckshop.pro')
    search_field = py.get('#smartSearch')
    assert search_field.type('golem').get_attribute('value') == 'golem'
    assert search_field.clear().get_attribute('value') == ''


def test_children(py):
    py.visit('https://deckshop.pro')
    first_row_of_cards_in_deck = py.get("[href*='/deck/detail/'] > span").children()
    assert first_row_of_cards_in_deck.length == 4
