@needs_py39
def test_update(client: TestClient):
    response = client.put("/items/foo", json={"name": "Wrestlers"})
    assert response.status_code == 200, response.text
    assert response.json() == {"name": "Wrestlers", "size": None}