def test_coerce():
    response = client.get("/items/coerce")
    response.raise_for_status()
    assert response.json() == {
        "name": "coerce",
        "date": datetime(2021, 7, 26).isoformat(),
        "price": 1.0,
        "owner_ids": None,
    }