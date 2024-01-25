def test_get_user(client):
    response = client.get("/users/1")
    assert response.status_code == 200, response.text
    data = response.json()
    assert "email" in data
    assert "id" in data