def test_response_model_model1_annotation_model2_return_submodel_with_extra_data():
    response = client.get(
        "/response_model_model1-annotation_model2-return_submodel_with_extra_data"
    )
    assert response.status_code == 200, response.text
    assert response.json() == {"name": "John", "surname": "Doe"}