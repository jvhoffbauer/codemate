def test_get_with_body():
    body = {"name": "Foo", "description": "Some description", "price": 5.5}
    response = client.request("GET", "/product", json=body)
    assert response.json() == body