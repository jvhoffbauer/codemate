def test_security_api_key():
    client = TestClient(app, cookies={"key": "secret"})
    response = client.get("/users/me")
    assert response.status_code == 200, response.text
    assert response.json() == {"username": "secret"}