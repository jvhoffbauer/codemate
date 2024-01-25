def test_websocket_invalid_path_doesnt_match():
    with pytest.raises(WebSocketDisconnect):
        with client.websocket_connect("/itemsx/portal-gun"):
            pass