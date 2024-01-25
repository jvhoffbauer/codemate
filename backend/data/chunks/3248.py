def test_objectlist():
    response = client.get("/items/objectlist")
    response.raise_for_status()
    assert response.json() == [
        {
            "name": "foo",
            "date": datetime(2021, 7, 26).isoformat(),
            "price": None,
            "owner_ids": None,
        },
        {
            "name": "bar",
            "date": datetime(2021, 7, 26).isoformat(),
            "price": 1.0,
            "owner_ids": None,
        },
        {
            "name": "baz",
            "date": datetime(2021, 7, 26).isoformat(),
            "price": 2.0,
            "owner_ids": [1, 2, 3],
        },
    ]