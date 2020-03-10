URL = 'http://the-internet.herokuapp.com'


def test_check_single_box(py):
    py.visit(f'{URL}/checkboxes')
    assert py.get('[type="checkbox"]').check().is_checked() is True
    assert py.get('[type="checkbox"]').uncheck().is_checked() is False


def test_check_many_boxes(py):
    py.visit(f'{URL}/checkboxes')
    assert py.find('[type="checkbox"]').check(allow_selected=True).are_checked()
