def test_path_param_le_3():
    response = client.get("/path/param-le/3")
    assert response.status_code == 200
    assert response.json() == 3