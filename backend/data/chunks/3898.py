def test_get_items():
    response = client.get("/keyword-weights/")
    assert response.status_code == 200, response.text
    assert response.json() == {"foo": 2.3, "bar": 3.4}