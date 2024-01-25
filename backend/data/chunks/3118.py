def test_router_depends_q_foo():
    response = client.get("/router-depends/?q=foo")
    assert response.status_code == 200
    assert response.json() == {
        "in": "router-depends",
        "params": {"q": "foo", "skip": 0, "limit": 100},
    }