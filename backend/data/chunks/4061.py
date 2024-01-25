@needs_py39
def test_query_params_str_validations_q_fixedquery(client: TestClient):
    response = client.get("/items/", params={"q": "fixedquery"})
    assert response.status_code == 200
    assert response.json() == {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}