def test_use_access_token(superuser_token_headers):
    server_api = get_server_api()
    r = requests.post(
        f"{server_api}{config.API_V1_STR}/login/test-token",
        headers=superuser_token_headers,
    )
    result = r.json()
    assert r.status_code == 200
    assert "username" in result