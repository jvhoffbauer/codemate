def test_return_defaults():
    response = client.get("/")
    assert response.json() == {"sub": {}}