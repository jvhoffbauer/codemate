@needs_py39
def test_items_bar_token_jessica(client: TestClient):
    response = client.get(
        "/items/bar?token=jessica", headers={"X-Token": "fake-super-secret-token"}
    )
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}