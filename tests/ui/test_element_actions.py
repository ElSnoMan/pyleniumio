import pytest
from selenium.common.exceptions import NoSuchElementException
from pylenium import jquery
from pylenium.driver import Pylenium
from pylenium.element import Element


THE_INTERNET = 'https://the-internet.herokuapp.com'


@pytest.fixture
def dropdown(py: Pylenium) -> Element:
    py.visit(f'{THE_INTERNET}/dropdown')
    return py.get('#dropdown')


def test_check_single_box(py):
    py.visit(f'{THE_INTERNET}/checkboxes')
    assert py.get('[type="checkbox"]').check().should().be_checked()
    assert py.get('[type="checkbox"]').uncheck().is_checked() is False


def test_check_many_boxes(py):
    py.visit(f'{THE_INTERNET}/checkboxes')
    assert py.find('[type="checkbox"]').check(allow_selected=True).are_checked()


def test_select_by_index_fails_if_option_not_available(dropdown: Element):
    with pytest.raises(NoSuchElementException):
        dropdown.select_by_index(3)


def test_select_by_text_fails_if_option_not_available(dropdown: Element):
    with pytest.raises(NoSuchElementException):
        dropdown.select_by_value('Option 3')


def test_select_by_value_fails_if_option_not_available(dropdown: Element):
    with pytest.raises(NoSuchElementException):
        dropdown.select_by_value('3')


def test_select_by_index(dropdown: Element):
    dropdown.select_by_index(1)
    assert dropdown.getx('./option[2]').should().be_selected()


def test_select_by_text(dropdown: Element):
    dropdown.select_by_text('Option 1')
    assert dropdown.getx('./option[2]').should().be_selected()


def test_select_by_value(dropdown: Element):
    dropdown.select_by_value('2')
    assert dropdown.getx('./option[3]').should().be_selected()


def test_drag_to_with_selector(py):
    py.visit('https://the-internet.herokuapp.com/drag_and_drop')
    py.get('#column-a').drag_to('#column-b')
    assert py.get('#column-b > header').should().have_text('A')


def test_drag_to_with_element(py):
    py.visit('https://the-internet.herokuapp.com/drag_and_drop')
    column_b = py.get('#column-b')
    py.get('#column-a').drag_to_element(column_b)
    assert column_b.get('header').should().have_text('A')


def test_jquery(py):
    py.visit('https://amazon.com')
    jquery.inject(py.webdriver, version='3.5.1')
    assert py.execute_script('return jQuery.expando;') is not None
    assert py.execute_script('return $.expando;') is not None
    assert jquery.exists(py.webdriver) == '3.5.1'


def test_hover(py):
    py.visit('https://the-internet.herokuapp.com/hovers')
    assert py.get('.figure').hover().contains('View profile').should().be_visible()


def test_radio_buttons(py):
    py.visit('http://test.rubywatir.com/radios.php')
    radio = py.get('#radioId')
    assert radio.check().should().be_checked()

    py.get('[value="Radio1"]').check()
    assert not radio.is_checked()


def test_checkbox_buttons(py):
    py.visit('http://test.rubywatir.com/checkboxes.php')
    checkbox = py.get('input[name=sports][value=soccer]')
    assert checkbox.should().be_checked()

    checkbox.uncheck()
    assert not checkbox.is_checked()
