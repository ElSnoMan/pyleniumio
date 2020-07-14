from pytest_bdd import scenarios, when, parsers
from selenium.webdriver.common.keys import Keys

scenarios('../feature/driver.feature')


@when(parsers.parse('I search {query}'))
def i_search(py, query):
    py.get("[name='q']").type(query, Keys.ENTER)


@when('I open the Leadership Page')
def open_leadership_page(py):
    py.get("a[href='/about']").hover()
    py.get("a[href='/leadership'][class*='Header']").click()
