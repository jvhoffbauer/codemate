def test_security_api_key_no_key():
    client = TestClient(app)
    response = client.get("/users/me")
    assert response.status_code == 403, response.text
    assert response.json() == {"detail": "Not authenticated"}