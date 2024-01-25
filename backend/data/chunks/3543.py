def test_path_param_le_ge_int_2():
    response = client.get("/path/param-le-ge-int/2")
    assert response.status_code == 200
    assert response.json() == 2