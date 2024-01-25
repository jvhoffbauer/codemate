def test_path_param_min_maxlength_foo():
    response = client.get("/path/param-min_maxlength/foo")
    assert response.status_code == 200
    assert response.json() == "foo"