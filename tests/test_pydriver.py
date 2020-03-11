from selenium.webdriver.common.keys import Keys


def test_execute_script(py):
    py.visit('https://google.com')
    webelement = py.get("[name='q']").webelement
    assert py.execute_script('return arguments[0].parentNode;', webelement)


def test_google_search(py):
    py.visit('https://google.com')
    py.get("[name='q']").type('puppies', Keys.ENTER)
    assert 'puppies' in py.title


def test_cookies(py):
    cookie_to_set = {'name': 'foo', 'value': 'bar'}
    cookie_to_test = {
        'domain': 'www.google.com',
        'httpOnly': False,
        'name': 'foo',
        'path': '/',
        'secure': True,
        'value': 'bar'
    }
    py.visit('https://google.com')

    py.set_cookie(cookie_to_set)
    assert py.get_cookie('foo') == cookie_to_test

    py.delete_cookie('foo')
    assert py.get_cookie('foo') is None
