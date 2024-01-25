def test_batch_notify(echo, raw_request):
    resp = raw_request(
        json_dumps(
            [
                {
                    "jsonrpc": "2.0",
                    "method": "echo",
                    "params": {"data": "data-111"},
                },
                {
                    "jsonrpc": "2.0",
                    "method": "echo",
                    "params": {"data": "data-222"},
                },
            ]
        )
    )
    assert not resp.content
    assert set(echo.history) == {"data-111", "data-222"}