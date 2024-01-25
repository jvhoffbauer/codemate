def test_get_users(client):
    response = client.get("/users/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert "email" in data[0]
    assert "id" in data[0]