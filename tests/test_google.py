from selenium.webdriver.common.keys import Keys


def test_google_search(driver):
    driver.visit('https://google.com')
    driver.get("[name='q']").type('puppies', Keys.ENTER)
    assert 'puppies' in driver.title
