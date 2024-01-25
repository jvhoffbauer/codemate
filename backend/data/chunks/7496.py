def test_admin_add_auth(client: TestClient, superuser_token_headers: dict):
    """
    测试管理员设置权限是否被拦截
    :return:
    """
    response = client.post(
        "/add/auth",
        json={"authority_id": "100", "path": "/add/auth", "method": "POST"},
        headers=superuser_token_headers,
    )
    assert response.status_code == 200
    assert response.json()["code"] == 200