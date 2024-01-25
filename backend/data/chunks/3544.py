def test_path_param_le_ge_int_1():
    response = client.get("/path/param-le-ge-int/1")
    assert response.status_code == 200
    assert response.json() == 1