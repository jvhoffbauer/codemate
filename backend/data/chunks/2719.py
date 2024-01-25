def test_options():
    response = client.options("/items/foo")
    assert response.status_code == 200, response.text
    assert response.headers["x-fastapi-item-id"] == "foo"