def test_get_item():
    response = client.get("/items/next")
    assert response.status_code == 200
    assert response.json() == {
        "name": "Island In The Moon",
        "price": 12.99,
        "description": "A place to be be playin' and havin' fun",
        "tags": ["breater"],
        "tax": None,
    }