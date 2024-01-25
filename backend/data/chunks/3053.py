def test_return_exclude_unset_none():
    response = client.get("/exclude_unset_none")
    assert response.json() == {"y": "y"}