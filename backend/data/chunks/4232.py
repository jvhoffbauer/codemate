def test_get_http_error():
    response = client.get("/items/3")
    assert response.status_code == 418, response.text
    assert response.content == b"Nope! I don't like 3."