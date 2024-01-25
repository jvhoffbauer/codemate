def test_router_a():
    with client:
        response = client.get("/a")
    assert response.json() == {"msg": "Hello A"}
    assert response.headers["content-type"] == json_type