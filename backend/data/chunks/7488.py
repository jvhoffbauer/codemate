def test_login(client: TestClient) -> None:
    """
    测试登录
    自行使用 /app/create_user.py 创建任意测试用户
    test@test.com
    test
    :return:
    """
    response = client.post(
        "/admin/auth/login/access-token",
        json={"username": "test@test.com", "password": "test"},
    )
    assert response.status_code == 200
    assert response.json()["code"] == 200
    assert response.json()["data"]["token"]