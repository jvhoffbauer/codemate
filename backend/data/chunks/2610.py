def test_model_with_tuple_invalid():
    data = {"items": [["foo", "bar"], ["baz", "whatelse", "too", "much"]]}
    response = client.post("/model-with-tuple/", json=data)
    assert response.status_code == 422, response.text

    data = {"items": [["foo", "bar"], ["baz"]]}
    response = client.post("/model-with-tuple/", json=data)
    assert response.status_code == 422, response.text