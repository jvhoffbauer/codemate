def test_validlist_exclude_unset():
    response = client.get("/items/validlist-exclude-unset")
    response.raise_for_status()
    assert response.json() == [
        {"aliased_name": "foo"},
        {"aliased_name": "bar", "price": 1.0},
        {"aliased_name": "baz", "price": 2.0, "owner_ids": [1, 2, 3]},
    ]