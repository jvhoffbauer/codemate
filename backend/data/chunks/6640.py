async def test_auth_refresh_token(client: AsyncClient, default_user: User):
    response = await client.post(
        app.url_path_for("login_access_token"),
        data={
            "username": default_user_email,
            "password": default_user_password,
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    refresh_token = response.json()["refresh_token"]

    new_token_response = await client.post(
        app.url_path_for("refresh_token"), json={"refresh_token": refresh_token}
    )
    assert new_token_response.status_code == codes.OK
    token = new_token_response.json()
    assert token["token_type"] == "Bearer"
    assert "access_token" in token
    assert "expires_at" in token
    assert "issued_at" in token
    assert "refresh_token" in token
    assert "refresh_token_expires_at" in token
    assert "refresh_token_issued_at" in token