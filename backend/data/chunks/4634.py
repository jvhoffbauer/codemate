@needs_py310
def test_query_params_str_validations(client: TestClient):
    response = client.post("/items/", json={"name": "Foo", "price": 42})
    assert response.status_code == 200, response.text
    assert response.json() == {
        "name": "Foo",
        "price": 42,
        "description": None,
        "tax": None,
        "tags": [],
    }