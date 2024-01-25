def test_coerce_exclude_unset():
    response = client.get("/items/coerce-exclude-unset")
    response.raise_for_status()
    assert response.json() == {"aliased_name": "coerce", "price": 1.0}