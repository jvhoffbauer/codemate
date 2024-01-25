def test_get(url, data, client: TestClient):
    response = client.get(url)
    assert response.status_code == 200, response.text
    assert response.json() == data