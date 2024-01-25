def test_read_model():
    response = client.get("/model")
    assert response.status_code == 200, response.text
    assert response.json() == {"name": "Foo"}