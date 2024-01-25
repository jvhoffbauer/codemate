def test_login():
    response = client.post("/token", data={"username": "johndoe", "password": "secret"})
    assert response.status_code == 200, response.text
    content = response.json()
    assert "access_token" in content
    assert content["token_type"] == "bearer"