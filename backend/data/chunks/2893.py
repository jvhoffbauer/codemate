def test_get_users_item():
    """Check that /users/{user_id}/items returns expected data"""
    response = client.get("/users/abc123/items/item01")
    assert response.status_code == 200, response.text
    assert response.json() == {"item_id": "item01", "user_id": "abc123"}