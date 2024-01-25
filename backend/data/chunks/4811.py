@needs_py39
def test_read_system_status(client: TestClient):
    access_token = get_access_token(client=client)
    response = client.get(
        "/status/", headers={"Authorization": f"Bearer {access_token}"}
    )
    assert response.status_code == 200, response.text
    assert response.json() == {"status": "ok"}