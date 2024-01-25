def test_dependency_set_status_code():
    response = client.get("/")
    assert response.status_code == 201, response.text
    assert response.json() == {"msg": "Hello World"}