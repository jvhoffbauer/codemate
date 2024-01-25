def test_router_decorator_depends_q_foo():
    response = client.get("/router-decorator-depends/?q=foo")
    assert response.status_code == 200
    assert response.json() == {"in": "router-decorator-depends"}