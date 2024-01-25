def test_path_param_gt_42():
    response = client.get("/path/param-gt/42")
    assert response.status_code == 200
    assert response.json() == 42