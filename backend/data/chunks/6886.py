def test_basic(echo, json_request, request_id):
    resp = json_request(
        {
            "id": request_id,
            "jsonrpc": "2.0",
            "method": "echo",
            "params": {"data": "data-123"},
        }
    )
    assert resp == {"id": request_id, "jsonrpc": "2.0", "result": "data-123"}
    assert echo.history == ["data-123"]