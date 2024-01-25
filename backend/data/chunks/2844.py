def test_no_response_model_annotation_return_exact_dict():
    response = client.get("/no_response_model-annotation-return_exact_dict")
    assert response.status_code == 200, response.text
    assert response.json() == {"name": "John", "surname": "Doe"}