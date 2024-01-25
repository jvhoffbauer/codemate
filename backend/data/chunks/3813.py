@needs_py39
def test_items_token_jessica(client: TestClient):
    response = client.get(
        "/items?token=jessica", headers={"X-Token": "fake-super-secret-token"}
    )
    assert response.status_code == 200
    assert response.json() == {
        "plumbus": {"name": "Plumbus"},
        "gun": {"name": "Portal Gun"},
    }