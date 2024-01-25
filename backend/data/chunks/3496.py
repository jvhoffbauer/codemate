def test_path_param_foo():
    response = client.get("/path/param/foo")
    assert response.status_code == 200
    assert response.json() == "foo"