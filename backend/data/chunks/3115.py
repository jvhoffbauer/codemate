def test_decorator_depends_q_foo():
    response = client.get("/decorator-depends/?q=foo")
    assert response.status_code == 200
    assert response.json() == {"in": "decorator-depends"}