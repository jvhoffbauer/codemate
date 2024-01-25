@needs_py310
def test_token(client: TestClient):
    response = client.get("/users/me", headers={"Authorization": "Bearer johndoe"})
    assert response.status_code == 200, response.text
    assert response.json() == {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    }