def test_get_items_2():
    """Check that /items returns expected data with user_id specified"""
    response = client.get("/items?user_id=abc123")
    assert response.status_code == 200, response.text
    assert response.json() == [{"item_id": "i2", "user_id": "abc123"}]