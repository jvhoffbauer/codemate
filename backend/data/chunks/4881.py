@needs_py310
def test_login(client: TestClient):
    response = client.post("/token", data={"username": "johndoe", "password": "secret"})
    assert response.status_code == 200, response.text
    assert response.json() == {"access_token": "johndoe", "token_type": "bearer"}