import pytest


def test_element_with_no_siblings(py):
    py.visit('https://deckshop.pro')
    elements = py.get("a[href='/spy/']").siblings()
    assert elements.should().be_empty()


def test_element_parent_and_siblings(py):
    py.visit('https://deckshop.pro')
    parent = py.get("a.nav-link[href='/spy/']").parent()
    assert parent.tag_name() == 'li'
    assert parent.siblings().should().have_length(8)


def test_element_text(py):
    py.visit('https://deckshop.pro')
    assert py.contains('Season').should().have_text('Season 11!')


def test_find_in_element_context(py):
    py.visit('https://deckshop.pro')
    headers = py.find('h5')
    assert headers[1].get('a').should().contain_text('Loon Cycle')


def test_input_type_and_get_value(py):
    py.visit('https://deckshop.pro')
    search_field = py.get('#smartSearch')
    assert search_field.type('golem').should().have_value('golem')
    assert search_field.clear().should().have_value('')


def test_children(py):
    py.visit('https://deckshop.pro')
    first_row_of_cards_in_deck = py.get("[href*='/deck/detail/'] > span").children()
    assert first_row_of_cards_in_deck.should().have_length(4)


def test_forced_click(py):
    py.visit('https://amazon.com')
    # without forcing, this raises ElementNotInteractableException
    py.get_xpath("//*[@class='nav-title and text()='Your Account']").click(force=True)


def test_element_should_be_clickable(py):
    py.visit('https://deckshop.pro')
    assert py.get("a.nav-link[href='/spy/']").should().be_clickable()


def test_element_should_not_be_clickable(py):
    py.visit('https://deckshop.pro')
    with pytest.raises(AssertionError):
        py.get('#smartHelp').should().be_visible()


def test_element_should_be_visible(py):
    py.visit('http://book.theautomatedtester.co.uk/chapter1')
    py.get('#loadajax').click()
    assert py.get('#ajaxdiv').should().be_visible()


def test_element_should_be_hidden(py):
    py.visit('https://deckshop.pro')
    assert py.get('#smartHelp').should().be_hidden()


def test_element_should_be_focused(py):
    py.visit('https://deckshop.pro')
    py.get('#smartSearch').click()
    assert py.get('#smartSearch').should().be_focused()


def test_element_should_not_be_focused(py):
    py.visit('https://deckshop.pro')
    assert py.get('#smartSearch').should().not_be_focused()


def test_elements_should_be_empty(py):
    py.visit('https://google.com')
    assert py.find('select', timeout=3).should().be_empty()
    assert py.find_xpath('//select', timeout=0).should().be_empty()


def test_elements_should_not_be_empty(py):
    py.visit('https://the-internet.herokuapp.com/add_remove_elements/')
    py.contains('Add Element').click()
    py.contains('Add Element').click()
    assert py.find('.added-manually').should().not_be_empty()


def test_elements_should_have_length(py):
    py.visit('https://the-internet.herokuapp.com/add_remove_elements/')
    py.contains('Add Element').click()
    py.contains('Add Element').click()
    assert py.find('.added-manually').should().have_length(2)


def test_elements_should_be_greater_than(py):
    py.visit('https://the-internet.herokuapp.com/add_remove_elements/')
    py.contains('Add Element').click()
    py.contains('Add Element').click()
    assert py.find('.added-manually').should().be_greater_than(1)


def test_elements_should_be_less_than(py):
    py.visit('https://the-internet.herokuapp.com/add_remove_elements/')
    py.contains('Add Element').click()
    py.contains('Add Element').click()
    assert py.find('.added-manually').should().be_less_than(3)


def test_element_attribute(py):
    search_field = '[name="q"]'
    py.visit('https://google.com')
    assert py.get(search_field).get_attribute('title') == 'Search'
    assert py.get(search_field).should().have_attr('title', 'Search')


def test_element_property(py):
    search_field = '[name="q"]'
    py.visit('https://google.com')
    assert py.get(search_field).get_property('maxLength') == 2048
    assert py.get(search_field).should().have_prop('maxLength', 2048)


def test_element_should_disappear(py):
    spinner = '#serverSideDataTable_processing'
    py.visit('https://www.copart.com/lotSearchResults/?free=true&query=nissan')
    assert py.get(spinner).should().disappear()


def test_element_has_attribute(py):
    py.visit('http://the-internet.herokuapp.com/checkboxes')
    py.find('[type="checkbox"]')[1].should().have_attr('checked')


def test_element_does_not_have_attribute(py):
    py.visit('http://the-internet.herokuapp.com/checkboxes')
    py.get('[type="checkbox"]').should().not_have_attr('checked')


def test_element_has_attribute_with_value(py):
    py.visit('http://the-internet.herokuapp.com/checkboxes')
    py.get('[type="checkbox"]').should().have_attr('type', 'checkbox')


def test_element_does_not_have_attribute_with_value(py):
    py.visit('http://the-internet.herokuapp.com/checkboxes')
    py.get('[type="checkbox"]').should().not_have_attr('type', 'box')
