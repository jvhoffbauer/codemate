def test_response_model_none_annotation_return_invalid_dict():
    response = client.get("/response_model_none-annotation-return_invalid_dict")
    assert response.status_code == 200, response.text
    assert response.json() == {"name": "John"}