def test_override_in_users_with_q():
    from docs_src.dependency_testing.tutorial001_an_py310 import client

    response = client.get("/users/?q=foo")
    assert response.status_code == 200, response.text
    assert response.json() == {
        "message": "Hello Users!",
        "params": {"q": "foo", "skip": 5, "limit": 10},
    }