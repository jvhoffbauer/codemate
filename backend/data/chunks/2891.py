def test_get_item_2():
    """Check that /items/{item_id} returns expected data with user_id specified"""
    response = client.get("/items/item01?user_id=abc123")
    assert response.status_code == 200, response.text
    assert response.json() == {"item_id": "item01", "user_id": "abc123"}