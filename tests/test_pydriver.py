import pytest
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


def test_viewport(py):
    py.visit('https://google.com')
    py.viewport(1280, 800)
    assert {'width': 1280, 'height': 800} == py.window_size


def test_failed_screenshot(py):
    py.visit('https://google.com')
    py.get('[name="q"]').type('QA at the Point')
    pytest.fail('to trigger teardown screenshot')


def test_find_single_element_with_xpath(py):
    py.visit('https://google.com')
    py.xpath('//*[@name="q"]').type('QA at the Point', Keys.ENTER)
    assert 'QA at the Point' in py.title


def test_find_elements_with_xpath(py):
    py.visit('https://deckshop.pro')
    assert py.xpath('//a[@class="nav-link"]').length > 1
