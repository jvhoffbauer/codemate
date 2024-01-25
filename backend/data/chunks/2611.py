def test_tuple_with_model_valid():
    data = [{"x": 1, "y": 2}, {"x": 3, "y": 4}]
    response = client.post("/tuple-of-models/", json=data)
    assert response.status_code == 200, response.text
    assert response.json() == data