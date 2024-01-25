def test_create_item(client: TestClient) -> None:
    response = client.post("/items/", json={"name": "Foo"})
    assert response.status_code == 200, response.text
    assert response.json() == {"name": "Foo", "description": None}