def test_api_fixture(api):
    response = api.get('https://google.com')
    assert response.ok
