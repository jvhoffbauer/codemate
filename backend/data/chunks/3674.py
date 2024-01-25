def test_app():
    response = client.get("/foo")
    assert response.status_code == 200, response.text