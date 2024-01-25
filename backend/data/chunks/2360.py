def test_invalid_method_doesnt_match():
    response = client.post("/users/rick")
    assert response.status_code == 405, response.text