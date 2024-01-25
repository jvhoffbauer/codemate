def test_hidden_cookie(path, cookies, expected_status, expected_response):
    client = TestClient(app, cookies=cookies)
    response = client.get(path)
    assert response.status_code == expected_status
    assert response.json() == expected_response