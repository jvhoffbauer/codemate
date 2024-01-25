def test_valid():
    response = client.get("/items/valid")
    response.raise_for_status()
    assert response.json() == {"aliased_name": "valid", "price": 1.0, "owner_ids": None}