def test_path_param_minlength_foo():
    response = client.get("/path/param-minlength/foo")
    assert response.status_code == 200
    assert response.json() == "foo"