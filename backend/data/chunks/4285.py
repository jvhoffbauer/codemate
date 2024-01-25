@needs_py39
def test_websocket_no_credentials(app: FastAPI):
    client = TestClient(app)
    with pytest.raises(WebSocketDisconnect):
        with client.websocket_connect("/items/foo/ws"):
            pytest.fail(
                "did not raise WebSocketDisconnect on __enter__"
            )  # pragma: no cover