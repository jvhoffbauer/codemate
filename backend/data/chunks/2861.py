def test_response_model_filtering_model_annotation_submodel_return_submodel():
    response = client.get(
        "/response_model_filtering_model-annotation_submodel-return_submodel"
    )
    assert response.status_code == 200, response.text
    assert response.json() == {"name": "John", "surname": "Doe"}