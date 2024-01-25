def test_path_bool_False():
    response = client.get("/path/bool/False")
    assert response.status_code == 200
    assert response.json() is False