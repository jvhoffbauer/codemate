def test_response_model_none_annotation_return_invalid_model():
    response = client.get("/response_model_none-annotation-return_invalid_model")
    assert response.status_code == 200, response.text
    assert response.json() == {"name": "Foo", "price": 42.0}