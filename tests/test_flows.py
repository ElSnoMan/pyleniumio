
def test_add_to_cart(py):
    py.visit('https://jane.com')
    py.get('[data-testid="deal-image"]').click()

    for dropdown in py.find('select'):
        dropdown.select(1)

    py.get('[data-testid="add-to-bag"]', timeout=1).click()
    assert py.contains("$00.11")


def test_add_to_cart_xpath(py):
    py.visit('https://jane.com')
    py.getx('//*[@data-testid="deal-image"]').click()

    for dropdown in py.findx('//select'):
        dropdown.select(1)

    py.getx('//*[@data-testid="add-to-bag"]', timeout=1).click()
    assert py.contains("$00.11")
