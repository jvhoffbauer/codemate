def test_read_users():
    response = client.get("/users/42")
    assert response.status_code == 200, response.text