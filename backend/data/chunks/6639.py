async def test_auth_access_token_fail_no_user(client: AsyncClient):
    response = await client.post(
        app.url_path_for("login_access_token"),
        data={
            "username": "xxx",
            "password": "yyy",
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )

    assert response.status_code == codes.BAD_REQUEST
    assert response.json() == {"detail": "Incorrect email or password"}