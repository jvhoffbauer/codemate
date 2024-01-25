def test_login_incorrect_username(client: TestClient):
    response = client.post("/token", data={"username": "foo", "password": "secret"})
    assert response.status_code == 400, response.text
    assert response.json() == {"detail": "Incorrect username or password"}