def test_items_5(client: TestClient):
    response = client.put("/items/5", json={"item": {"name": "Foo", "price": 3.0}})
    assert response.status_code == 200
    assert response.json() == {
        "item_id": 5,
        "item": {"name": "Foo", "price": 3.0, "description": None, "tax": None},
    }