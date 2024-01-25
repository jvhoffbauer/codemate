def test_path_param_lt0__1():
    response = client.get("/path/param-lt0/-1")
    assert response.status_code == 200
    assert response.json() == -1