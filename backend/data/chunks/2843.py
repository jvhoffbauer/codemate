def test_no_response_model_annotation_return_same_model():
    response = client.get("/no_response_model-annotation-return_same_model")
    assert response.status_code == 200, response.text
    assert response.json() == {"name": "John", "surname": "Doe"}