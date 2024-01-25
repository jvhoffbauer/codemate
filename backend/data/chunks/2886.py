def test_get_users():
    """Check that /users returns expected data"""
    response = client.get("/users")
    assert response.status_code == 200, response.text
    assert response.json() == [{"user_id": "u1"}, {"user_id": "u2"}]