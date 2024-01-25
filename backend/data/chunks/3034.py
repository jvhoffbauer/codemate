def test_override_security():
    app.dependency_overrides[get_user] = get_user_override
    response = client.get("/user")
    assert response.json() == {
        "user": "alice",
        "scopes": ["foo", "bar"],
        "data": [1, 2, 3],
    }
    app.dependency_overrides = {}