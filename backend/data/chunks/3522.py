def test_path_param_le_ge_1():
    response = client.get("/path/param-le-ge/1")
    assert response.status_code == 200