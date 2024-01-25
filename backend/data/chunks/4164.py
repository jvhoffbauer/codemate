def test_post():
    response = client.post("/items/", content=b"this is actually not validated")
    assert response.status_code == 200, response.text
    assert response.json() == {
        "size": 30,
        "content": {
            "name": "Maaaagic",
            "price": 42,
            "description": "Just kiddin', no magic here. ✨",
        },
    }