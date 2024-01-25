def test_async_state():
    assert state["/async"] == "asyncgen not started"
    response = client.get("/async")
    assert response.status_code == 200, response.text
    assert response.json() == "asyncgen started"
    assert state["/async"] == "asyncgen completed"