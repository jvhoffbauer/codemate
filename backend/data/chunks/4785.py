@needs_py39
def test_incorrect_token(client: TestClient):
    response = client.get("/items", headers={"Authorization": "Notexistent testtoken"})
    assert response.status_code == 401, response.text
    assert response.json() == {"detail": "Not authenticated"}
    assert response.headers["WWW-Authenticate"] == "Bearer"