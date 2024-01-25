def test_depend_validation():
    """
    Verify that a validation in a dependency invokes the correct exception handler
    """
    caught = []

    @websocket_middleware
    async def catcher(websocket, call_next):
        try:
            return await call_next()
        except Exception as e:  # pragma: no cover
            caught.append(e)
            raise

    myapp = make_app(middleware=[Middleware(catcher)])

    client = TestClient(myapp)
    with pytest.raises(WebSocketDisconnect) as e:
        with client.websocket_connect("/depends-validate/"):
            pass  # pragma: no cover
    # the validation error does produce a close message
    assert e.value.code == status.WS_1008_POLICY_VIOLATION
    # and no error is leaked
    assert caught == []