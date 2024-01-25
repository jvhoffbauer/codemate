def test_response_model_union_no_annotation_return_model2():
    response = client.get("/response_model_union-no_annotation-return_model2")
    assert response.status_code == 200, response.text
    assert response.json() == {"name": "Foo", "price": 42.0}