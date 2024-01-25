def test_get_user(client: TestClient, ordinary_token_headers: dict):
    """
    测试获取用户信息的接口
    :return:
    """
    response = client.get("/admin/auth/user/info", headers=ordinary_token_headers)

    assert response.status_code == 200
    assert response.json()["code"] == 200
    assert isinstance(response.json()["data"]["nickname"], str)