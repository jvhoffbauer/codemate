def test_no_response_model_annotation_union_return_model1():
    response = client.get("/no_response_model-annotation_union-return_model1")
    assert response.status_code == 200, response.text
    assert response.json() == {"name": "John", "surname": "Doe"}