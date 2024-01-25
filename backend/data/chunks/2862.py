def test_response_model_list_of_model_no_annotation():
    response = client.get("/response_model_list_of_model-no_annotation")
    assert response.status_code == 200, response.text
    assert response.json() == [
        {"name": "John", "surname": "Doe"},
        {"name": "Jane", "surname": "Does"},
    ]