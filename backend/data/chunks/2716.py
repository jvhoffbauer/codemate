def test_get_api_route_not_decorated():
    response = client.get("/items-not-decorated/foo")
    assert response.status_code == 200, response.text
    assert response.json() == {"item_id": "foo"}