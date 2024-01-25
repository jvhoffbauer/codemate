def test_default_param_query():
    response = client.get("/items/?q=foo")
    assert response.status_code == 200, response.text
    assert response.json() == {"q": "foo"}