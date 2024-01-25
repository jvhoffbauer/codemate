def test_valid():
    response = client.get("/items/valid")
    response.raise_for_status()
    assert response.json() == {
        "name": "valid",
        "date": datetime(2021, 7, 26).isoformat(),
        "price": 1.0,
        "owner_ids": None,
    }