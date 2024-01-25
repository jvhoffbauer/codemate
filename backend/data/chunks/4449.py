def test_override_in_users_with_params():
    from docs_src.dependency_testing.tutorial001_an_py310 import client

    response = client.get("/users/?q=foo&skip=100&limit=200")
    assert response.status_code == 200, response.text
    assert response.json() == {
        "message": "Hello Users!",
        "params": {"q": "foo", "skip": 5, "limit": 10},
    }