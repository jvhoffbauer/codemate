def test_validdict():
    response = client.get("/items/validdict")
    response.raise_for_status()
    assert response.json() == {
        "k1": {"aliased_name": "foo", "price": None, "owner_ids": None},
        "k2": {"aliased_name": "bar", "price": 1.0, "owner_ids": None},
        "k3": {"aliased_name": "baz", "price": 2.0, "owner_ids": [1, 2, 3]},
    }