@needs_py310
def test_create(client: TestClient):
    response = client.put("/items/red", json={"name": "Chillies"})
    assert response.status_code == 201, response.text
    assert response.json() == {"name": "Chillies", "size": None}