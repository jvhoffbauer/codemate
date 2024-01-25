def test_default_param_query_none():
    response = client.get("/items/")
    assert response.status_code == 200, response.text
    assert response.json() == {"q": None}