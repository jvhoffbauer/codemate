def test_native_prefix_router():
    client = TestClient(app)
    with client.websocket_connect("/native/") as websocket:
        data = websocket.receive_text()
        assert data == "Hello, router with native prefix!"