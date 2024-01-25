def test_get_users_items():
    """Check that /users/{user_id}/items returns expected data"""
    response = client.get("/users/abc123/items")
    assert response.status_code == 200, response.text
    assert response.json() == [{"item_id": "i2", "user_id": "abc123"}]