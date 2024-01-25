def test_path_int_42():
    response = client.get("/path/int/42")
    assert response.status_code == 200
    assert response.json() == 42