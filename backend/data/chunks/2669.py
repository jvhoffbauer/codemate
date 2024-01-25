def test_response():
    # For coverage
    response = client.get("/foo")
    assert response.status_code == 200, response.text
    assert response.json() == {"name": "Foo item"}