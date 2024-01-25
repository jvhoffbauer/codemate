async def test_auth_access_token(client: AsyncClient, default_user: User):
    response = await client.post(
        app.url_path_for("login_access_token"),
        data={
            "username": default_user_email,
            "password": default_user_password,
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    assert response.status_code == codes.OK
    token = response.json()
    assert token["token_type"] == "Bearer"
    assert "access_token" in token
    assert "expires_at" in token
    assert "issued_at" in token
    assert "refresh_token" in token
    assert "refresh_token_expires_at" in token
    assert "refresh_token_issued_at" in token