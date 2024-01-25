def test_no_response_model_annotation_list_of_model():
    response = client.get("/no_response_model-annotation_list_of_model")
    assert response.status_code == 200, response.text
    assert response.json() == [
        {"name": "John", "surname": "Doe"},
        {"name": "Jane", "surname": "Does"},
    ]