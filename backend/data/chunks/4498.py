def test_get_users():
    response = client.get("/users/foo")
    assert response.status_code == 200, response.text
    assert response.json() == {"message": "Hello foo"}