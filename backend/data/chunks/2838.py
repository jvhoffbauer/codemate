def test_response_model_no_annotation_return_exact_dict():
    response = client.get("/response_model-no_annotation-return_exact_dict")
    assert response.status_code == 200, response.text
    assert response.json() == {"name": "John", "surname": "Doe"}