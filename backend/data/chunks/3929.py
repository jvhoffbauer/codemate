def test_flask():
    response = client.get("/v1/")
    assert response.status_code == 200, response.text
    assert response.text == "Hello, World from Flask!"