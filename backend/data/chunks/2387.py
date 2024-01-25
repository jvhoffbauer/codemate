def test_validdict_exclude_unset():
    response = client.get("/items/validdict-exclude-unset")
    response.raise_for_status()
    assert response.json() == {
        "k1": {"aliased_name": "foo"},
        "k2": {"aliased_name": "bar", "price": 1.0},
        "k3": {"aliased_name": "baz", "price": 2.0, "owner_ids": [1, 2, 3]},
    }