def test_router_ws_depends_with_override():
    client = TestClient(app)
    app.dependency_overrides[ws_dependency] = lambda: "Override"  # noqa: E731
    with client.websocket_connect("/router-ws-depends/") as websocket:
        assert websocket.receive_text() == "Override"