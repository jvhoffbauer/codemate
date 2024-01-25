def test_token_no_scope(client: TestClient):
    access_token = get_access_token(client=client)
    response = client.get(
        "/users/me", headers={"Authorization": f"Bearer {access_token}"}
    )
    assert response.status_code == 401, response.text
    assert response.json() == {"detail": "Not enough permissions"}
    assert response.headers["WWW-Authenticate"] == 'Bearer scope="me"'