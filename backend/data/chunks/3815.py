@needs_py39
def test_items_plumbus_token_jessica(client: TestClient):
    response = client.get(
        "/items/plumbus?token=jessica", headers={"X-Token": "fake-super-secret-token"}
    )
    assert response.status_code == 200
    assert response.json() == {"name": "Plumbus", "item_id": "plumbus"}