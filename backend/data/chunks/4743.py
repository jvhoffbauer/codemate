@needs_py310
def test_login_incorrect_password(client: TestClient):
    response = client.post(
        "/token", data={"username": "johndoe", "password": "incorrect"}
    )
    assert response.status_code == 400, response.text
    assert response.json() == {"detail": "Incorrect username or password"}