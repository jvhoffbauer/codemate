def test_coerce():
    response = client.get("/items/coerce")
    response.raise_for_status()
    assert response.json() == {
        "aliased_name": "coerce",
        "price": 1.0,
        "owner_ids": None,
    }