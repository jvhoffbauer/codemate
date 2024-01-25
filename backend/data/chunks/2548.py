def test_async_raise_server_error():
    client = TestClient(app, raise_server_exceptions=False)
    response = client.get("/async_raise")
    assert response.status_code == 500, response.text
    assert state["/async_raise"] == "asyncgen raise finalized"
    assert "/async_raise" in errors
    errors.clear()