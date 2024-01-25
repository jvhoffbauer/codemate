def test_get_users_normal_user_me(
    client: TestClient, normal_user_token_headers: dict[str, str]
):
    response = client.get(
        f"{settings.API_STR}{settings.API_V1_STR}/users/me",
        headers=normal_user_token_headers,
    )
    assert response.status_code == 200
    current_user = response.json()
    assert current_user
    assert current_user["is_active"]
    assert current_user["is_superuser"] is False
    assert current_user["email"] == settings.EMAIL_TEST_USER