def test_sync_sync_raise_server_error():
    client = TestClient(app, raise_server_exceptions=False)
    response = client.get("/sync_sync_raise")
    assert response.status_code == 500, response.text
    assert state["/sync_raise"] == "generator raise finalized"
    assert "/sync_raise" in errors
    errors.clear()