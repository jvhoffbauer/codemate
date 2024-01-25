def test_path_param_lt_gt_2():
    response = client.get("/path/param-lt-gt/2")
    assert response.status_code == 200
    assert response.json() == 2