from selenium.webdriver.common.keys import Keys


def test_google_search(py):
    py.visit('https://google.com')
    py.get("[name='q']").type('puppies', Keys.ENTER)
    assert 'puppies' in py.title
