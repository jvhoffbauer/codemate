def test_valid_exclude_unset():
    response = client.get("/items/valid-exclude-unset")
    response.raise_for_status()
    assert response.json() == {"aliased_name": "valid", "price": 1.0}