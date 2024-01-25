def test_router_b_a_override():
    with client:
        response = client.get("/b/a/override")
    assert response.content == b"Hello B A"
    assert response.headers["content-type"] == html_type