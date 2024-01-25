def test_api(client: TestClient):
    response = client.get("/users/john")
    assert response.status_code == 200, response.text
    assert response.json()["message"] == "Hello john"