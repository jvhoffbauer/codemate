def test_put(client: TestClient):
    response = client.put(
        "/items/bar", json={"name": "Barz", "price": 3, "description": None}
    )
    assert response.json() == {
        "name": "Barz",
        "description": None,
        "price": 3,
        "tax": 10.5,
        "tags": [],
    }