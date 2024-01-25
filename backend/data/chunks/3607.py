def test_routerindex():
    client = TestClient(app)
    with client.websocket_connect("/router") as websocket:
        data = json.loads(websocket.receive_text())
        assert data == ["app", "router2", "router", "routerindex"]