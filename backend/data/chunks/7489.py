def test_error_login(client: TestClient) -> None:
    """
    测试错误密码是否能登录
    test@test.com
    test
    :return:
    """
    response = client.post(
        "/admin/auth/login/access-token",
        json={"username": "test1@test.com", "password": "t"},
    )
    assert response.status_code == 200
    assert response.json()["code"] == 4003