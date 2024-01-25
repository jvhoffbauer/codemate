def test_path_foobar():
    response = client.get("/path/foobar")
    assert response.status_code == 200
    assert response.json() == "foobar"