def test_admin(client: TestClient):
    response = client.post(
        "/admin/?token=jessica", headers={"X-Token": "fake-super-secret-token"}
    )
    assert response.status_code == 200, response.text
    assert response.json() == {"message": "Admin getting schwifty"}