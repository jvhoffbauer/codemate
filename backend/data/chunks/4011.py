@needs_py39
def test_post_no_body(client: TestClient):
    response = client.put("/items/5", json=None)
    assert response.status_code == 200
    assert response.json() == {"item_id": 5}