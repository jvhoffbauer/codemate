def test_no_hidden_query():
    response = client.get("/items")
    assert response.status_code == 200, response.text
    assert response.json() == {"hidden_query": "Not found"}