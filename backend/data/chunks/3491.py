def test_path_bool_1():
    response = client.get("/path/bool/1")
    assert response.status_code == 200
    assert response.json() is True