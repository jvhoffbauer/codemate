def test_users_me_token_jessica(client: TestClient):
    response = client.get("/users/me?token=jessica")
    assert response.status_code == 200
    assert response.json() == {"username": "fakecurrentuser"}