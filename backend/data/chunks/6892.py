def test_request_method_validation_error(echo, json_request):
    resp = json_request(
        {
            "id": 0,
            "jsonrpc": "2.0",
            "method": 123,
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
                        "input": 123,
                        "loc": ["method"],
                        "msg": "Input should be a valid string",
                        "type": "string_type",
                    },
                ]
            },
        },
        "id": 0,
        "jsonrpc": "2.0",
    }
    assert echo.history == []