def test_method_not_found(echo, json_request):
    resp = json_request(
        {
            "id": 0,
            "jsonrpc": "2.0",
            "method": "echo-bla-bla",
            "params": {"data": "data-123"},
        }
    )
    assert resp == {
        "error": {"code": -32601, "message": "Method not found"},
        "id": 0,
        "jsonrpc": "2.0",
    }
    assert echo.history == []