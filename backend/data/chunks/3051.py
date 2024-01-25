def test_return_exclude_defaults():
    response = client.get("/exclude_defaults")
    assert response.json() == {}