def test_get():
    response = client.get("/users/rick")
    assert response.status_code == 200, response.text
    assert response.json() == {"user_id": "rick", "path": "/users/{user_id}"}