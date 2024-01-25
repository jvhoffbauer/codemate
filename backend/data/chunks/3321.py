def test_get_response():
    response = client.get("/a")
    assert response.status_code == 204, response.text
    assert "content-length" not in response.headers
    assert response.content == b""