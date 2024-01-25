@needs_py39
def test_items_bar_with_invalid_token(client: TestClient):
    response = client.get("/items/bar?token=jessica", headers={"X-Token": "invalid"})
    assert response.status_code == 400
    assert response.json() == {"detail": "X-Token header invalid"}