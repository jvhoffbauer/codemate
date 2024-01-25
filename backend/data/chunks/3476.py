def test_path_str_foobar():
    response = client.get("/path/str/foobar")
    assert response.status_code == 200
    assert response.json() == "foobar"