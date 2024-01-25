def test_read_item_name(client: TestClient):
    response = client.get("/items/bar/name")
    assert response.status_code == 200, response.text
    assert response.json() == {"name": "Bar", "description": "The Bar fighters"}