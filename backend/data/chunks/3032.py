def test_normal():
    response = client.get("/user")
    assert response.json() == {
        "user": "john",
        "scopes": ["foo", "bar"],
        "data": [1, 2, 3],
    }