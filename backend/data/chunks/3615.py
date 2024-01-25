def test_valid_none_none():
    response = client.get("/items/validnone", params={"send_none": "true"})
    data = response.json()
    assert response.status_code == 200
    assert data is None