def test_return_exclude_unset():
    response = client.get("/exclude_unset")
    assert response.json() == {"x": None, "y": "y"}