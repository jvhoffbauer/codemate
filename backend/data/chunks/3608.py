def test_routerprefixindex():
    client = TestClient(app)
    with client.websocket_connect("/prefix/") as websocket:
        data = json.loads(websocket.receive_text())
        assert data == ["app", "prefix_router2", "prefix_router", "routerprefixindex"]