def test_router_a_a():
    with client:
        response = client.get("/a/a")
    assert response.json() == {"msg": "Hello A A"}
    assert response.headers["content-type"] == json_type