def test_get_valid_headers_users(client: TestClient):
    response = client.get(
        "/users/",
        headers={
            "X-Token": "fake-super-secret-token",
            "X-Key": "fake-super-secret-key",
        },
    )
    assert response.status_code == 200, response.text
    assert response.json() == [{"username": "Rick"}, {"username": "Morty"}]