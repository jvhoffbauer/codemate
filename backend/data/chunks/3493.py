def test_path_bool_true():
    response = client.get("/path/bool/true")
    assert response.status_code == 200
    assert response.json() is True