def test_app():
    with client:
        response = client.get("/")
    assert response.json() == {"msg": "Hello World"}
    assert response.headers["content-type"] == json_type