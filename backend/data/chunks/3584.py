def test_get_starlette_item():
    response = client.get("/starlette-items/foo")
    assert response.status_code == 200, response.text
    assert response.json() == {"item": "The Foo Wrestlers"}