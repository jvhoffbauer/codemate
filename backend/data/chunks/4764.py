def test_token_no_username(client: TestClient):
    response = client.get(
        "/users/me",
        headers={
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJmb28ifQ.NnExK_dlNAYyzACrXtXDrcWOgGY2JuPbI4eDaHdfK5Y"
        },
    )
    assert response.status_code == 401, response.text
    assert response.json() == {"detail": "Could not validate credentials"}
    assert response.headers["WWW-Authenticate"] == 'Bearer scope="me"'