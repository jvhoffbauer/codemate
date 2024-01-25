def test_depend_err_handler():
    """
    Verify that it is possible to write custom WebSocket middleware to catch errors
    """

    async def custom_handler(websocket: WebSocket, exc: CustomError) -> None:
        await websocket.close(1002, "foo")

    myapp = make_app(exception_handlers={CustomError: custom_handler})
    client = TestClient(myapp)
    with pytest.raises(WebSocketDisconnect) as e:
        with client.websocket_connect("/custom_error/"):
            pass  # pragma: no cover
    assert e.value.code == 1002
    assert "foo" in e.value.reason