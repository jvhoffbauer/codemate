def test_validlist():
    response = client.get("/items/validlist")
    response.raise_for_status()
    assert response.json() == [
        {"aliased_name": "foo", "price": None, "owner_ids": None},
        {"aliased_name": "bar", "price": 1.0, "owner_ids": None},
        {"aliased_name": "baz", "price": 2.0, "owner_ids": [1, 2, 3]},
    ]