@needs_py39
def test_users_foo_token_jessica(client: TestClient):
    response = client.get("/users/foo?token=jessica")
    assert response.status_code == 200
    assert response.json() == {"username": "foo"}