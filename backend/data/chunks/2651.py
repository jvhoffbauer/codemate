def test_router_with_params():
    client = TestClient(app)
    with client.websocket_connect(
        "/router/path/to/file?queryparam=a_query_param"
    ) as websocket:
        data = websocket.receive_text()
        assert data == "path/to/file"
        data = websocket.receive_text()
        assert data == "a_query_param"