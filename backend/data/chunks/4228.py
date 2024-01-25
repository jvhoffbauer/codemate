def test_get_item_header():
    response = client.get("/items-header/foo")
    assert response.status_code == 200, response.text
    assert response.json() == {"item": "The Foo Wrestlers"}