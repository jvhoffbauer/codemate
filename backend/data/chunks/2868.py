def test_no_response_model_annotation_union_return_model2():
    response = client.get("/no_response_model-annotation_union-return_model2")
    assert response.status_code == 200, response.text
    assert response.json() == {"name": "Foo", "price": 42.0}