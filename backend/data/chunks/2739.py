def test_strict_login_correct_correct_grant_type():
    response = client.post(
        "/login",
        data={"username": "johndoe", "password": "secret", "grant_type": "password"},
    )
    assert response.status_code == 200, response.text
    assert response.json() == {
        "grant_type": "password",
        "username": "johndoe",
        "password": "secret",
        "scopes": [],
        "client_id": None,
        "client_secret": None,
    }