def test_router_decorator_depends_q_foo_skip_100_limit_200():
    response = client.get("/router-decorator-depends/?q=foo&skip=100&limit=200")
    assert response.status_code == 200
    assert response.json() == {"in": "router-decorator-depends"}