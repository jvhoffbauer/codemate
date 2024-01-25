def test_get_user():
    """Check that /users/{user_id} returns expected data"""
    response = client.get("/users/abc123")
    assert response.status_code == 200, response.text
    assert response.json() == {"user_id": "abc123"}