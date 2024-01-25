def test_path_param_ge_3():
    response = client.get("/path/param-ge/3")
    assert response.status_code == 200
    assert response.json() == 3