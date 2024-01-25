@pytest.mark.parametrize(
    "path,cookies,expected_status,expected_response",
    [
        (
            "/hidden_cookie",
            {},
            200,
            {"hidden_cookie": None},
        ),
        (
            "/hidden_cookie",
            {"hidden_cookie": "somevalue"},
            200,
            {"hidden_cookie": "somevalue"},
        ),
    ],
)
def test_hidden_cookie(path, cookies, expected_status, expected_response):
    client = TestClient(app, cookies=cookies)
    response = client.get(path)
    assert response.status_code == expected_status
    assert response.json() == expected_response