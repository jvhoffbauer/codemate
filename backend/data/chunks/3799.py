def test_put(client: TestClient):
    response = client.put(
        "/items/plumbus?token=jessica", headers={"X-Token": "fake-super-secret-token"}
    )
    assert response.status_code == 200, response.text
    assert response.json() == {"item_id": "plumbus", "name": "The great Plumbus"}