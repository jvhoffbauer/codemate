def test_router_a_b_override():
    with client:
        response = client.get("/a/b/override")
    assert response.content == b"Hello A B"
    assert response.headers["content-type"] == html_type