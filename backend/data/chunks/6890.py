def test_request_jsonrpc_validation_error(echo, json_request):
    resp = json_request(
        {
            "id": 0,
            "jsonrpc": "3.0",
            "method": "echo",
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
                        "ctx": {"expected": "'2.0'"},
                        "input": "3.0",
                        "loc": ["jsonrpc"],
                        "msg": "Input should be '2.0'",
                        "type": "literal_error",
                    }
                ]
            },
        },
        "id": 0,
        "jsonrpc": "2.0",
    }
    assert echo.history == []