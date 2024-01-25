def test_path_bool_True():
    response = client.get("/path/bool/True")
    assert response.status_code == 200
    assert response.json() is True