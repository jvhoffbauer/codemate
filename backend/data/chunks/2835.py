def test_no_response_model_no_annotation_return_model():
    response = client.get("/no_response_model-no_annotation-return_model")
    assert response.status_code == 200, response.text
    assert response.json() == {"name": "John", "surname": "Doe"}