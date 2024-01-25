def test_router_a_b():
    with client:
        response = client.get("/a/b")
    assert response.content == b"Hello A B"
    assert response.headers["content-type"] == text_type