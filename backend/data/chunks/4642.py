def test_get(path, expected_status, expected_response, client: TestClient):
    response = client.get(path)
    assert response.status_code == expected_status
    assert response.json() == expected_response