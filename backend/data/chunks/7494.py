def test_ordinary_add_auth(client: TestClient, ordinary_token_headers: dict):
    """
    测试普通用户设置权限是否被拦截
    :return:
    """
    response = client.post(
        "/add/auth",
        json={"authority_id": "100", "path": "/add/auth", "method": "POST"},
        headers=ordinary_token_headers,
    )

    assert response.status_code == 200
    assert response.json()["code"] == 4003