def test_hidden_query():
    response = client.get("/items?hidden_query=somevalue")
    assert response.status_code == 200, response.text
    assert response.json() == {"hidden_query": "somevalue"}