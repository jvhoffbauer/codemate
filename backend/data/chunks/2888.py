def test_get_items_1():
    """Check that /items returns expected data"""
    response = client.get("/items")
    assert response.status_code == 200, response.text
    assert response.json() == [
        {"item_id": "i1", "user_id": "u1"},
        {"item_id": "i2", "user_id": "u2"},
    ]