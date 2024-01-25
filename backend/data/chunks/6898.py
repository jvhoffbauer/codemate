def test_batch(echo, json_request):
    resp = json_request(
        [
            {
                "id": 111,
                "jsonrpc": "2.0",
                "method": "echo",
                "params": {"data": "data-111"},
            },
            {
                "jsonrpc": "2.0",
                "method": "echo",
                "params": {"data": "data-notify"},
            },
            {
                "id": "qwe",
                "jsonrpc": "2.0",
                "method": "echo",
                "params": {"data": "data-qwe"},
            },
            {
                "id": "method-not-found",
                "jsonrpc": "2.0",
                "method": "echo-bla-bla",
                "params": {"data": "data-123"},
            },
        ]
    )
    assert resp == [
        {"id": 111, "jsonrpc": "2.0", "result": "data-111"},
        {"id": "qwe", "jsonrpc": "2.0", "result": "data-qwe"},
        {
            "id": "method-not-found",
            "jsonrpc": "2.0",
            "error": {"code": -32601, "message": "Method not found"},
        },
    ]
    assert set(echo.history) == {"data-111", "data-notify", "data-qwe"}