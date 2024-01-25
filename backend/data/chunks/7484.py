@pytest.fixture(scope="module")
def superuser_token_headers(client: TestClient) -> dict:
    """
    管理员 admin 用户测试， 后续新增 一份测试环境
    :param client:
    :return:
    """
    return user_authentication_headers(
        client=client, email="admin@admin.com", password="admin"
    )