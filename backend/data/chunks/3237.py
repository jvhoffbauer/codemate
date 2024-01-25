def get_validlist():
    return [
        {"name": "foo", "date": datetime(2021, 7, 26)},
        {"name": "bar", "date": datetime(2021, 7, 26), "price": 1.0},
        {
            "name": "baz",
            "date": datetime(2021, 7, 26),
            "price": 2.0,
            "owner_ids": [1, 2, 3],
        },
    ]