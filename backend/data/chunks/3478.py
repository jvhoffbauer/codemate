def test_path_str_True():
    response = client.get("/path/str/True")
    assert response.status_code == 200
    assert response.json() == "True"