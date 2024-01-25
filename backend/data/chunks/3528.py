def test_path_param_gt_int_42():
    response = client.get("/path/param-gt-int/42")
    assert response.status_code == 200
    assert response.json() == 42