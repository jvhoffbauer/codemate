def test_main_depends_q_foo_skip_100_limit_200():
    response = client.get("/main-depends/?q=foo&skip=100&limit=200")
    assert response.status_code == 200
    assert response.json() == {
        "in": "main-depends",
        "params": {"q": "foo", "skip": 100, "limit": 200},
    }