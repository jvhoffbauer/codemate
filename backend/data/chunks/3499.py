def test_path_param_maxlength_foo():
    response = client.get("/path/param-maxlength/foo")
    assert response.status_code == 200
    assert response.json() == "foo"