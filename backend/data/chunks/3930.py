def test_app():
    response = client.get("/v2")
    assert response.status_code == 200, response.text
    assert response.json() == {"message": "Hello World"}