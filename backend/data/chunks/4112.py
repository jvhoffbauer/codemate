def test_query_no_values():
    url = "/items/"
    response = client.get(url)
    assert response.status_code == 200, response.text
    assert response.json() == {"q": None}