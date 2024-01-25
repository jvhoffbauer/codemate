def test_router_a_override():
    with client:
        response = client.get("/a/override")
    assert response.content == b"Hello A"
    assert response.headers["content-type"] == text_type