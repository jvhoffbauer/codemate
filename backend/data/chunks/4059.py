@needs_py39
def test_query_params_str_validations_item_query_fixedquery(client: TestClient):
    response = client.get("/items/", params={"item-query": "fixedquery"})
    assert response.status_code == 200
    assert response.json() == {
        "items": [{"item_id": "Foo"}, {"item_id": "Bar"}],
        "q": "fixedquery",
    }