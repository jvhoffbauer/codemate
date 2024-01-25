def test_path_float_42_5():
    response = client.get("/path/float/42.5")
    assert response.status_code == 200
    assert response.json() == 42.5