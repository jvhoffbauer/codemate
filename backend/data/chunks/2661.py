def test_depend_err_middleware():
    """
    Verify that it is possible to write custom WebSocket middleware to catch errors
    """

    @websocket_middleware
    async def errorhandler(websocket: WebSocket, call_next):
        try:
            return await call_next()
        except Exception as e:
            await websocket.close(code=status.WS_1006_ABNORMAL_CLOSURE, reason=repr(e))

    myapp = make_app(middleware=[Middleware(errorhandler)])
    client = TestClient(myapp)
    with pytest.raises(WebSocketDisconnect) as e:
        with client.websocket_connect("/depends-err/"):
            pass  # pragma: no cover
    assert e.value.code == status.WS_1006_ABNORMAL_CLOSURE
    assert "NotImplementedError" in e.value.reason