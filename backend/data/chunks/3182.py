def test_router_b_a_c():
    with client:
        response = client.get("/b/a/c")
    assert response.content == b"Hello B A C"
    assert response.headers["content-type"] == html_type