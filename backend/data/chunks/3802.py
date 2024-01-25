def test_admin_invalid_header(client: TestClient):
    response = client.post("/admin/", headers={"X-Token": "invalid"})
    assert response.status_code == 400, response.text
    assert response.json() == {"detail": "X-Token header invalid"}