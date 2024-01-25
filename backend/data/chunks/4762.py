def test_token_no_sub(client: TestClient):
    response = client.get(
        "/users/me",
        headers={
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjoiZm9vIn0.9ynBhuYb4e6aW3oJr_K_TBgwcMTDpRToQIE25L57rOE"
        },
    )
    assert response.status_code == 401, response.text
    assert response.json() == {"detail": "Could not validate credentials"}
    assert response.headers["WWW-Authenticate"] == 'Bearer scope="me"'