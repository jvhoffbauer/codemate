def test_response():
    response = client.get("/items/")
    assert response.json() == {"id": "foo"}