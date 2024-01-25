def test_index():
    client = TestClient(app)
    with client.websocket_connect("/") as websocket:
        data = json.loads(websocket.receive_text())
        assert data == ["app", "index"]