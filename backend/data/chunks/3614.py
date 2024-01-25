def test_valid_none_data():
    response = client.get("/items/validnone")
    data = response.json()
    assert response.status_code == 200
    assert data == {"name": "invalid", "price": 3.2, "owner_ids": None}