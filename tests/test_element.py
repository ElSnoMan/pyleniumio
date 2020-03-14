
class TestElements:
    """ Tests in this class are run sequentially and from top to bottom.

    Warnings:
        This approach is NOT recommended. Your tests should be modular, atomic and deterministic

    * These tests are sharing the same instance of Pylenium
    * The Logger treats this class (or suite) as a single Test, so only one log.txt is created
    """
    def test_element_with_no_siblings(self, pyc):
        pyc.visit('https://deckshop.pro')
        elements = pyc.get("[href='/spy/']").siblings()
        assert elements.length == 0

    def test_element_parent_and_siblings(self, pyc):
        parent = pyc.get("a.nav-link[href='/spy/']").parent()
        assert parent.tag_name == 'li'
        assert parent.siblings().length == 8

    def test_element_text(self, pyc):
        assert pyc.contains('More info').text == 'More info'

    def test_find_in_element_context(self, pyc):
        headers = pyc.find('h5')
        assert 'Royal Delivery' in headers[1].get("a").text

    def test_input_type_and_get_value(self, pyc):
        search_field = pyc.get('#smartSearch')
        assert search_field.type('golem').get_attribute('value') == 'golem'
        assert search_field.clear().get_attribute('value') == ''

    def test_children(self, pyc):
        first_row_of_cards_in_deck = pyc.get("[href*='/deck/detail/'] > span").children()
        assert first_row_of_cards_in_deck.length == 4
