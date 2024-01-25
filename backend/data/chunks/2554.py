def test_sync_async_state():
    response = client.get("/sync_async")
    assert response.status_code == 200, response.text
    assert response.json() == "asyncgen started"
    assert state["/async"] == "asyncgen completed"