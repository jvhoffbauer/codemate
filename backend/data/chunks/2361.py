def test_invalid_path_doesnt_match():
    response = client.post("/usersx/rick")
    assert response.status_code == 404, response.text