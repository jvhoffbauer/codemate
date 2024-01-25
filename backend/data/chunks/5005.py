@needs_pydanticv1
def test_filter_sub_model(client: TestClient):
    response = client.get("/model/modelA")
    assert response.status_code == 200, response.text
    assert response.json() == {
        "name": "modelA",
        "description": "model-a-desc",
        "model_b": {"username": "test-user"},
    }