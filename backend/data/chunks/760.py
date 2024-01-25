async def test_websocket_request(caplog, app):
    """
    We expect websocket requests to not be handled.
    This test could use improvement.
    """

    @app.websocket_route("/ws")
    async def websocket(websocket: "WebSocket"):
        # Check we get the right headers back
        assert websocket.headers.get("x-request-id") is not None

        await websocket.accept()
        await websocket.send_json({"msg": "Hello WebSocket"})
        await websocket.close()

    client = TestClient(app)
    with client.websocket_connect("/ws") as ws:
        ws.receive_json()
        assert caplog.messages == []