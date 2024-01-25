def test_get_custom_response():
    response = client.get("/items/")
    assert response.status_code == 200, response.text
    assert response.json() == [{"item_id": "Foo"}]