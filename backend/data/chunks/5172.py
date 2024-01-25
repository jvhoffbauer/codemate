def test_get_users_normal_user_me(normal_user_token_headers):
    server_api = get_server_api()
    r = requests.get(
        f"{server_api}{config.API_V1_STR}/users/me", headers=normal_user_token_headers
    )
    current_user = r.json()
    assert current_user
    assert current_user["disabled"] is False
    assert "superuser" not in current_user["admin_roles"]
    assert current_user["email"] == config.EMAIL_TEST_USER