def test_wrong_uri():
    """
    Verify that a websocket connection to a non-existent endpoing returns in a shutdown
    """
    client = TestClient(app)
    with pytest.raises(WebSocketDisconnect) as e:
        with client.websocket_connect("/no-router/"):
            pass  # pragma: no cover
    assert e.value.code == status.WS_1000_NORMAL_CLOSURE