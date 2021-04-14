import pytest
from pylenium.driver import Pylenium
from selenium.common.exceptions import ElementNotInteractableException


THE_INTERNET = 'https://the-internet.herokuapp.com'
DEMO_QA = 'https://demoqa.com'


def test_element_with_no_siblings(py: Pylenium):
    py.visit(f'{THE_INTERNET}/dropdown')
    elements = py.get('#page-footer > div').siblings()
    assert elements.should().be_empty()


def test_element_parent_and_siblings(py: Pylenium):
    py.visit(f'{DEMO_QA}/menu')
    parent = py.contains('Main Item 1').parent()
    assert parent.tag_name() == 'li'
    assert parent.siblings().should().have_length(2)


def test_element_text(py: Pylenium):
    py.visit(f'{DEMO_QA}/text-box')
    assert py.get('#userName-label').should().have_text('Full Name')


def test_find_in_element_context(py: Pylenium):
    py.visit(f'{DEMO_QA}/menu')
    menu_2 = py.contains('Main Item 2')
    items = menu_2.parent().find('li')
    assert items.should().have_length(5)


def test_input_type_and_get_value(py: Pylenium):
    py.visit('https://deckshop.pro')
    search_field = py.get('#smartSearch')
    assert search_field.type('golem').should().have_value('golem')
    assert search_field.clear().should().have_value('')


def test_children(py: Pylenium):
    py.visit(f'{THE_INTERNET}/dropdown')
    options = py.get('#dropdown').children()
    assert options.should().have_length(3)


def test_forced_click(py: Pylenium):
    py.visit(f'{DEMO_QA}/checkbox')
    # without forcing, this raises ElementNotInteractableException
    py.get("[type='checkbox']").click(force=True)
    assert py.get('#result').should().contain_text('You have selected')


def test_element_should_be_clickable(py: Pylenium):
    py.visit(f'{DEMO_QA}/buttons')
    assert py.contains("Click Me").should().be_clickable()


def test_element_should_not_be_clickable(py: Pylenium):
    py.visit(f'{DEMO_QA}/checkbox')
    with pytest.raises(AssertionError):
        py.get('[type="checkbox"]').should(timeout=3).be_clickable()


def test_element_should_be_visible(py: Pylenium):
    py.visit('http://book.theautomatedtester.co.uk/chapter1')
    py.get('#loadajax').click()
    assert py.get('#ajaxdiv').should().be_visible()


def test_element_should_be_hidden(py: Pylenium):
    py.visit('https://deckshop.pro')
    assert py.get('#smartHelp').should().be_hidden()


def test_element_should_be_focused(py: Pylenium):
    py.visit('https://deckshop.pro')
    py.get('#smartSearch').click()
    assert py.get('#smartSearch').should().be_focused()


def test_element_should_not_be_focused(py: Pylenium):
    py.visit('https://deckshop.pro')
    assert py.get('#smartSearch').should().not_be_focused()


def test_elements_should_be_empty(py: Pylenium):
    py.visit('https://google.com')
    assert py.find('select', timeout=3).should().be_empty()
    assert py.findx('//select', timeout=0).should().be_empty()


def test_elements_should_not_be_empty(py: Pylenium):
    py.visit(f'{THE_INTERNET}/add_remove_elements/')
    py.contains('Add Element').click()
    py.contains('Add Element').click()
    assert py.find('.added-manually').should().not_be_empty()


def test_elements_should_have_length(py: Pylenium):
    py.visit(f'{THE_INTERNET}/add_remove_elements/')
    py.contains('Add Element').click()
    py.contains('Add Element').click()
    assert py.find('.added-manually').should().have_length(2)


def test_elements_should_be_greater_than(py: Pylenium):
    py.visit(f'{THE_INTERNET}/add_remove_elements/')
    py.contains('Add Element').click()
    py.contains('Add Element').click()
    assert py.find('.added-manually').should().be_greater_than(1)


def test_elements_should_be_less_than(py: Pylenium):
    py.visit(f'{THE_INTERNET}/add_remove_elements/')
    py.contains('Add Element').click()
    py.contains('Add Element').click()
    assert py.find('.added-manually').should().be_less_than(3)


def test_element_attribute(py: Pylenium):
    search_field = '[name="q"]'
    py.visit('https://google.com')
    assert py.get(search_field).get_attribute('title') == 'Search'
    assert py.get(search_field).should().have_attr('title', 'Search')


def test_element_property(py: Pylenium):
    search_field = '[name="q"]'
    py.visit('https://google.com')
    assert py.get(search_field).get_property('maxLength') == 2048
    assert py.get(search_field).should().have_prop('maxLength', 2048)


def test_element_should_disappear(py: Pylenium):
    spinner = '#serverSideDataTable_processing'
    py.visit('https://www.copart.com/lotSearchResults/?free=true&query=nissan')
    assert py.get(spinner).should().disappear()


def test_element_has_attribute(py: Pylenium):
    py.visit(f'{THE_INTERNET}/checkboxes')
    py.find('[type="checkbox"]')[1].should().have_attr('checked')


def test_element_does_not_have_attribute(py: Pylenium):
    py.visit(f'{THE_INTERNET}/checkboxes')
    py.get('[type="checkbox"]').should().not_have_attr('checked')


def test_element_has_attribute_with_value(py: Pylenium):
    py.visit(f'{THE_INTERNET}/checkboxes')
    py.get('[type="checkbox"]').should().have_attr('type', 'checkbox')


def test_element_does_not_have_attribute_with_value(py: Pylenium):
    py.visit(f'{THE_INTERNET}/checkboxes')
    py.should().contain_title('The Internet')
    py.get('[type="checkbox"]').should().not_have_attr('type', 'box')


def test_element_css_value(py: Pylenium):
    py.visit(f'{DEMO_QA}/buttons')
    element = py.contains('Click Me')
    assert element.css_value('backgroundColor') == "rgba(0, 123, 255, 1)"
    assert element.css_value('background-color') == "rgba(0, 123, 255, 1)"


def test_element_invalid_css_property_name(py: Pylenium):
    py.visit(f'{DEMO_QA}/buttons')
    element = py.contains('Click Me')
    assert element.css_value('bg-color') == ''
    assert element.css_value('length') is None


def test_getx_nested_element(py: Pylenium):
    py.visit(f'{DEMO_QA}/automation-practice-form')
    container = py.getx('//*[@id="subjectsContainer"]')
    element = container.getx('.//input')
    element_id = element.get_attribute('id')
    assert element_id == 'subjectsInput'


def test_findx_nested_element(py: Pylenium):
    py.visit(f'{DEMO_QA}/automation-practice-form')
    container = py.getx('//*[@id="hobbiesWrapper"]')
    elements = container.findx('.//input')
    assert len(elements) == 3
    for element in elements:
        assert element.get_attribute('type') == 'checkbox'
