def test_object():
    response = client.get("/items/object")
    response.raise_for_status()
    assert response.json() == {
        "name": "object",
        "date": datetime(2021, 7, 26).isoformat(),
        "price": 1.0,
        "owner_ids": [1, 2, 3],
    }