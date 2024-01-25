def test_router_b():
    with client:
        response = client.get("/b")
    assert response.content == b"Hello B"
    assert response.headers["content-type"] == text_type