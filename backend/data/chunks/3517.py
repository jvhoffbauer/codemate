def test_path_param_le_2():
    response = client.get("/path/param-le/2")
    assert response.status_code == 200
    assert response.json() == 2