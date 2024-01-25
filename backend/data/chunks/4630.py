def test_get_users():
    response = client.get("/users/")
    assert response.status_code == 200, response.text
    assert response.json() == ["Rick", "Morty"]