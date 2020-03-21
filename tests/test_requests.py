STATS_ROYALE_CARDS_API = 'https://statsroyale.com/api/cards'


def test_api_fixture(api):
    response = api.get('https://google.com')
    assert response.ok


def test_py_request(py):
    py.visit('https://statsroyale.com')
    response = py.request.get(STATS_ROYALE_CARDS_API)
    assert response.ok
    assert response.json()[0]['name']