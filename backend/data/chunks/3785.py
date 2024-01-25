def test_users_token_monica_with_no_jessica(client: TestClient):
    response = client.get("/users?token=monica")
    assert response.status_code == 400
    assert response.json() == {"detail": "No Jessica token provided"}