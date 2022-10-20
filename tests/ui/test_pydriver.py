import os
import pytest
from selenium.webdriver.common.by import By
from pylenium.a11y import PyleniumAxe
from pylenium.driver import Pylenium


THE_INTERNET = "https://the-internet.herokuapp.com"


def test_jit_webdriver(py: Pylenium):
    assert py._webdriver is None
    assert py.webdriver is not None
    assert py._webdriver is not None


@pytest.mark.skipif(os.environ.get("LT_USERNAME") is not None, reason="Doesn't work well with LambdaTest")
def test_browser_options(py: Pylenium):
    py.config.driver.options = ["--headless"]
    py.visit("https://google.com")
    assert py.should().contain_title("Google")


def test_execute_script(py: Pylenium):
    py.visit("https://google.com")
    webelement = py.get("[name='q']").webelement
    assert py.execute_script("return arguments[0].parentNode;", webelement)


def test_new_window_and_tab(py: Pylenium):
    py.switch_to.new_window()
    assert len(py.window_handles) == 2

    py.switch_to.new_tab()
    assert len(py.window_handles) == 3


def test_cookies(py: Pylenium):
    cookie_to_set = {"name": "foo", "value": "bar"}
    cookie_to_test = {
        "domain": "www.google.com",
        "httpOnly": False,
        "name": "foo",
        "path": "/",
        "secure": True,
        "value": "bar",
    }
    py.visit("https://google.com")

    py.set_cookie(cookie_to_set)
    assert py.get_cookie("foo") == cookie_to_test

    py.delete_cookie("foo")
    assert py.get_cookie("foo") is None


def test_viewport(py: Pylenium):
    py.visit("https://google.com")
    py.viewport(1280, 800)
    assert {"width": 1280, "height": 800} == py.window_size


def test_hover_and_click_to_page_transition(py: Pylenium):
    py.visit("https://qap.dev")
    py.get('a[href="/about"]').hover().get('a[href="/leadership"][class*=Header]').click()
    assert py.contains("Carlos Kidman").should().contain_text("Carlos Kidman")


def test_pylenium_wait_until(py: Pylenium):
    py.visit("https://qap.dev")
    py.wait(use_py=True).sleep(2)
    element = py.wait(5, use_py=True).until(lambda x: x.find_element(By.CSS_SELECTOR, '[href="/about"]'))
    assert element.tag_name() == "a"
    assert element.hover()


def test_webdriver_wait_until(py: Pylenium):
    py.visit("https://qap.dev")
    element = py.wait(5).until(lambda x: x.find_element(By.CSS_SELECTOR, '[href="/about"]'))
    assert element.tag_name == "a"


def test_switch_to_frame_by_element_then_back(py: Pylenium):
    py.visit(f"{THE_INTERNET}/iframe")
    iframe = py.get("#mce_0_ifr")
    py.switch_to.frame_by_element(iframe).get("#tinymce").clear().type("foo")
    assert py.switch_to.default_content().contains("An iFrame").tag_name() == "h3"
    py.switch_to.frame_by_element(iframe).get("#tinymce").type("bar")
    assert py.get("#tinymce").text() == "foobar"
    assert py.switch_to.parent_frame().contains("An iFrame").tag_name() == "h3"


def test_have_url(py: Pylenium):
    py.visit("https://qap.dev")
    py.should().have_url("https://www.qap.dev/")


@pytest.mark.skip(reason="Unstable test as of Selenium 4")
def test_loading_extension_to_browser(py: Pylenium, project_root):
    py.config.driver.extension_paths.append(f"{project_root}/tests/ui/Get CRX.crx")
    py.visit("chrome://extensions/")
    shadow1 = py.get("extensions-manager").open_shadow_dom()
    shadow2 = shadow1.get("extensions-item-list").open_shadow_dom()
    ext_shadow_dom = shadow2.find("extensions-item").first().open_shadow_dom()
    assert ext_shadow_dom.get("#name-and-version").should().contain_text("Get CRX")


def test_should_not_find(py: Pylenium):
    py.visit("https://google.com")
    assert py.should().not_find("select")
    assert py.should().not_findx("//select")
    assert py.should().not_contain("foobar")


def test_axe_run(py: Pylenium):
    py.visit("https://qap.dev")
    axe = PyleniumAxe(py.webdriver)
    report = axe.run(name="a11y.json")
    number_of_violations = len(report.violations)
    assert number_of_violations < 10, f"{number_of_violations} violation(s) found"


def test_axe_fixture(axe):
    axe.webdriver.get("https://qap.dev")
    file_name = "a11y.json"
    axe.run(name=file_name)
    assert os.path.exists(file_name)
