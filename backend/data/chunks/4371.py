@needs_py310
def test_items_6(client: TestClient):
    response = client.put(
        "/items/6",
        json={
            "item": {
                "name": "Bar",
                "price": 0.2,
                "description": "Some bar",
                "tax": "5.4",
            }
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "item_id": 6,
        "item": {
            "name": "Bar",
            "price": 0.2,
            "description": "Some bar",
            "tax": 5.4,
        },
    }