@needs_py39
def test_get_invalid_one_header_items(client: TestClient):
    response = client.get("/items/", headers={"X-Token": "invalid"})
    assert response.status_code == 400, response.text
    assert response.json() == {"detail": "X-Token header invalid"}