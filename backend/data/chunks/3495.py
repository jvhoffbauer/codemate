def test_path_bool_false():
    response = client.get("/path/bool/false")
    assert response.status_code == 200
    assert response.json() is False