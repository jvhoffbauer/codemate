def test_no_response_model_annotation_json_response_class():
    response = client.get("/no_response_model-annotation_json_response_class")
    assert response.status_code == 200, response.text
    assert response.json() == {"foo": "bar"}