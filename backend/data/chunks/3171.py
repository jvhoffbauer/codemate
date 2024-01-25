def test_app_override():
    with client:
        response = client.get("/override")
    assert response.content == b"Hello World"
    assert response.headers["content-type"] == text_type