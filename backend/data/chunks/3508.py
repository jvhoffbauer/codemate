def test_path_param_ge_42():
    response = client.get("/path/param-ge/42")
    assert response.status_code == 200
    assert response.json() == 42