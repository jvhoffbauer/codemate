def test_router_b_a_c_override():
    with client:
        response = client.get("/b/a/c/override")
    assert response.json() == {"msg": "Hello B A C"}
    assert response.headers["content-type"] == override_type