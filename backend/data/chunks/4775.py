@needs_py310
def test_read_system_status_no_token(client: TestClient):
    response = client.get("/status/")
    assert response.status_code == 401, response.text
    assert response.json() == {"detail": "Not authenticated"}
    assert response.headers["WWW-Authenticate"] == "Bearer"