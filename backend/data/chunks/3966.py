def test_read_item_public_data(client: TestClient):
    response = client.get("/items/bar/public")
    assert response.status_code == 200, response.text
    assert response.json() == {
        "name": "Bar",
        "description": "The Bar fighters",
        "price": 62,
    }