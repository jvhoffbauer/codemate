def test_sync_state():
    assert state["/sync"] == "generator not started"
    response = client.get("/sync")
    assert response.status_code == 200, response.text
    assert response.json() == "generator started"
    assert state["/sync"] == "generator completed"