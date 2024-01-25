def test_model_with_tuple_valid():
    data = {"items": [["foo", "bar"], ["baz", "whatelse"]]}
    response = client.post("/model-with-tuple/", json=data)
    assert response.status_code == 200, response.text
    assert response.json() == data