def test_multi_query_values():
    url = "/items/?q=foo&q=bar"
    response = client.get(url)
    assert response.status_code == 200, response.text
    assert response.json() == {"q": ["foo", "bar"]}