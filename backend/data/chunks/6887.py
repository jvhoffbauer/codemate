def test_notify(echo, raw_request):
    resp = raw_request(
        json_dumps(
            {
                "jsonrpc": "2.0",
                "method": "echo",
                "params": {"data": "data-123"},
            }
        )
    )
    assert not resp.content
    assert echo.history == ["data-123"]