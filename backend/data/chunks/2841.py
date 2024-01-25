def test_response_model_no_annotation_return_dict_with_extra_data():
    response = client.get("/response_model-no_annotation-return_dict_with_extra_data")
    assert response.status_code == 200, response.text
    assert response.json() == {"name": "John", "surname": "Doe"}