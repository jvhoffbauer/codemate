def test_router_ws_depends():
    client = TestClient(app)
    with client.websocket_connect("/router-ws-depends/") as websocket:
        assert websocket.receive_text() == "Socket Dependency"