def test_path_str_42():
    response = client.get("/path/str/42")
    assert response.status_code == 200
    assert response.json() == "42"