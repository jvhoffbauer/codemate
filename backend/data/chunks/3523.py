def test_path_param_le_ge_3():
    response = client.get("/path/param-le-ge/3")
    assert response.status_code == 200
    assert response.json() == 3