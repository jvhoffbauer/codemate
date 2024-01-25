def test_router_b_a():
    with client:
        response = client.get("/b/a")
    assert response.content == b"Hello B A"
    assert response.headers["content-type"] == text_type