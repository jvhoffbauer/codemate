def test_get(client: TestClient):
    response = client.get("/items/baz")
    assert response.status_code == 200, response.text
    assert response.json() == {
        "name": "Baz",
        "description": None,
        "price": 50.2,
        "tax": 10.5,
        "tags": [],
    }