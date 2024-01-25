def test_response_model_union_no_annotation_return_model1():
    response = client.get("/response_model_union-no_annotation-return_model1")
    assert response.status_code == 200, response.text
    assert response.json() == {"name": "John", "surname": "Doe"}