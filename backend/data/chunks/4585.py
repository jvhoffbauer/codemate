def test_path_operations():
    response = client.get("/items/")
    assert response.status_code == 200, response.text
    response = client.get("/users/")
    assert response.status_code == 200, response.text