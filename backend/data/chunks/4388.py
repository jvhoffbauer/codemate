def test_get():
    response = client.get("/")
    assert response.status_code == 200, response.text
    assert response.text == "Hello World"