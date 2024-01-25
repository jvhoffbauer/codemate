def test_inexistent_user(client):
    response = client.get("/users/999")
    assert response.status_code == 404, response.text