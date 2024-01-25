def test_heartbeat(test_client) -> None:
    response = test_client.get("/api/health/heartbeat")
    assert response.status_code == 200
    assert response.json() == {"is_alive": True}