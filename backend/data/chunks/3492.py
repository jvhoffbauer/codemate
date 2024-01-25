def test_path_bool_0():
    response = client.get("/path/bool/0")
    assert response.status_code == 200
    assert response.json() is False