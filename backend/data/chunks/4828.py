def test_login_incorrect_password():
    response = client.post(
        "/token", data={"username": "johndoe", "password": "incorrect"}
    )
    assert response.status_code == 400, response.text
    assert response.json() == {"detail": "Incorrect username or password"}