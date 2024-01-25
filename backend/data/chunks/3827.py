@needs_py39
def test_put_forbidden(client: TestClient):
    response = client.put(
        "/items/bar?token=jessica", headers={"X-Token": "fake-super-secret-token"}
    )
    assert response.status_code == 403, response.text
    assert response.json() == {"detail": "You can only update the item: plumbus"}