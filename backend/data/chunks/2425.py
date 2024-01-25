def test_multi_query():
    response = client.get("/items/?q=5&q=6")
    assert response.status_code == 200, response.text
    assert response.json() == {"q": [5, 6]}