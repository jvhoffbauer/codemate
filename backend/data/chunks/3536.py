def test_path_param_ge_int_3():
    response = client.get("/path/param-ge-int/3")
    assert response.status_code == 200
    assert response.json() == 3