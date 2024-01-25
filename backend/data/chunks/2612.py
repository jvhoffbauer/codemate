def test_tuple_with_model_invalid():
    data = [{"x": 1, "y": 2}, {"x": 3, "y": 4}, {"x": 5, "y": 6}]
    response = client.post("/tuple-of-models/", json=data)
    assert response.status_code == 422, response.text

    data = [{"x": 1, "y": 2}]
    response = client.post("/tuple-of-models/", json=data)
    assert response.status_code == 422, response.text