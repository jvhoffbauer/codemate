def test_request_method_missing(echo, json_request):
    resp = json_request(
        {
            "id": 0,
            "jsonrpc": "2.0",
            "params": {"data": "data-123"},
        }
    )
    assert resp == {
        "error": {
            "code": -32600,
            "message": "Invalid Request",
            "data": {
                "errors": [
                    {
                        "input": {
                            "id": 0,
                            "jsonrpc": "2.0",
                            "params": {"data": "data-123"},
                        },
                        "loc": ["method"],
                        "msg": "Field required",
                        "type": "missing",
                    }
                ]
            },
        },
        "id": 0,
        "jsonrpc": "2.0",
    }
    assert echo.history == []