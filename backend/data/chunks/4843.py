def test_read_system_status():
    access_token = get_access_token()
    response = client.get(
        "/status/", headers={"Authorization": f"Bearer {access_token}"}
    )
    assert response.status_code == 200, response.text
    assert response.json() == {"status": "ok"}