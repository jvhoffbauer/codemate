def test_post_items():
    response = client.post("/items/", json={"name": "Foo", "price": 5})
    assert response.status_code == 200, response.text
    assert response.json() == {"message": "Item received"}