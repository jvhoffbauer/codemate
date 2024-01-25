def test_get_item():
    response = client.get("/items/foo")
    assert response.status_code == 200, response.text
    assert response.json() == {"item": "The Foo Wrestlers"}