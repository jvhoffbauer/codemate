@needs_py39
def test_get_invalid_second_header_items(client: TestClient):
    response = client.get(
        "/items/", headers={"X-Token": "fake-super-secret-token", "X-Key": "invalid"}
    )
    assert response.status_code == 400, response.text
    assert response.json() == {"detail": "X-Key header invalid"}