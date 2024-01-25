def test_override_data():
    app.dependency_overrides[get_data] = get_data_override
    response = client.get("/user")
    assert response.json() == {
        "user": "john",
        "scopes": ["foo", "bar"],
        "data": [3, 4, 5],
    }
    app.dependency_overrides = {}