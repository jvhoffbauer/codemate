def test_path_float_42():
    response = client.get("/path/float/42")
    assert response.status_code == 200
    assert response.json() == 42