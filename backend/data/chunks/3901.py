def test_get_plane():
    response = client.get("/items/item2")
    assert response.status_code == 200, response.text
    assert response.json() == {
        "description": "Music is my aeroplane, it's my aeroplane",
        "type": "plane",
        "size": 5,
    }