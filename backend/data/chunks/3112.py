def test_main_depends_q_foo():
    response = client.get("/main-depends/?q=foo")
    assert response.status_code == 200
    assert response.json() == {
        "in": "main-depends",
        "params": {"q": "foo", "skip": 0, "limit": 100},
    }