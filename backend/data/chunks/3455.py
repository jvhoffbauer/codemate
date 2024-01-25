def test_hidden_header(path, headers, expected_status, expected_response):
    client = TestClient(app)
    response = client.get(path, headers=headers)
    assert response.status_code == expected_status
    assert response.json() == expected_response