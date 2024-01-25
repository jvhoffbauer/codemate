def test_sync_sync_state():
    response = client.get("/sync_sync")
    assert response.status_code == 200, response.text
    assert response.json() == "generator started"
    assert state["/sync"] == "generator completed"