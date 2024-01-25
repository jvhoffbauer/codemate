def test_router_b_override():
    with client:
        response = client.get("/b/override")
    assert response.content == b"Hello B"
    assert response.headers["content-type"] == html_type