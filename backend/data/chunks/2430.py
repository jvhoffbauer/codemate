def test_post_extended_item():
    response = client.post("/items/", json={"name": "Foo", "age": 5})
    assert response.status_code == 200, response.text
    assert response.json() == {"item": {"name": "Foo", "age": 5}}