def test_put_invalid_header(client: TestClient):
    response = client.put("/items/foo", headers={"X-Token": "invalid"})
    assert response.status_code == 400, response.text
    assert response.json() == {"detail": "X-Token header invalid"}