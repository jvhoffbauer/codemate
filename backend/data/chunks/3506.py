def test_path_param_gt0_0_05():
    response = client.get("/path/param-gt0/0.05")
    assert response.status_code == 200
    assert response.json() == 0.05