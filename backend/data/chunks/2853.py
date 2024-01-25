def test_response_model_none_annotation_return_dict_with_extra_data():
    response = client.get("/response_model_none-annotation-return_dict_with_extra_data")
    assert response.status_code == 200, response.text
    assert response.json() == {
        "name": "John",
        "surname": "Doe",
        "password_hash": "secret",
    }