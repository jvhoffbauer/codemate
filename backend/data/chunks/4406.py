def test_override_in_users():
    response = client.get("/users/")
    assert response.status_code == 200, response.text
    assert response.json() == {
        "message": "Hello Users!",
        "params": {"q": None, "skip": 5, "limit": 10},
    }