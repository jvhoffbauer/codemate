def test_path_param_le_ge_int_3():
    response = client.get("/path/param-le-ge-int/3")
    assert response.status_code == 200
    assert response.json() == 3