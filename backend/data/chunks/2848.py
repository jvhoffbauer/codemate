def test_no_response_model_annotation_return_submodel_with_extra_data():
    response = client.get(
        "/no_response_model-annotation-return_submodel_with_extra_data"
    )
    assert response.status_code == 200, response.text
    assert response.json() == {"name": "John", "surname": "Doe"}