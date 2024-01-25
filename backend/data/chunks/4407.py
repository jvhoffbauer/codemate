def test_override_in_users_with_q():
    response = client.get("/users/?q=foo")
    assert response.status_code == 200, response.text
    assert response.json() == {
        "message": "Hello Users!",
        "params": {"q": "foo", "skip": 5, "limit": 10},
    }