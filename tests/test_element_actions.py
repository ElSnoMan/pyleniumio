URL = 'http://the-internet.herokuapp.com'


def test_check_single_box(py):
    py.visit(f'{URL}/checkboxes')
    assert py.get('[type="checkbox"]').check().should().be_checked()
    assert py.get('[type="checkbox"]').uncheck().is_checked() is False


def test_check_many_boxes(py):
    py.visit(f'{URL}/checkboxes')
    assert py.find('[type="checkbox"]').check(allow_selected=True).are_checked()


def test_select_dropdown(py):
    py.visit(f'{URL}/dropdown')
    py.get('#dropdown').select('2')


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
    py.load_jquery('3.5.1')
    assert py.execute_script('return jQuery.expando;') is not None
    assert py.execute_script('return $.expando;') is not None


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
