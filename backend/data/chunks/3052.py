def test_return_exclude_none():
    response = client.get("/exclude_none")
    assert response.json() == {"y": "y", "z": "z"}