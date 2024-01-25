def test_websocket():
    with pytest.raises(WebSocketDisconnect):
        with client.websocket_connect("/ws") as websocket:
            message = "Message one"
            websocket.send_text(message)
            data = websocket.receive_text()
            assert data == f"Message text was: {message}"
            message = "Message two"
            websocket.send_text(message)
            data = websocket.receive_text()
            assert data == f"Message text was: {message}"