def test_post_with_str_float(client: TestClient):
    response = client.post("/items/", json={"name": "Foo", "price": "50.5"})
    assert response.status_code == 200
    assert response.json() == {
        "name": "Foo",
        "price": 50.5,
        "description": None,
        "tax": None,
    }