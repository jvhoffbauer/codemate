def test_request_id_validation_error(echo, json_request):
    resp = json_request(
        {
            "id": [123],
            "jsonrpc": "2.0",
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
                        "input": [123],
                        "loc": ["id", "str"],
                        "msg": "Input should be a valid string",
                        "type": "string_type",
                    },
                    {
                        "input": [123],
                        "loc": ["id", "int"],
                        "msg": "Input should be a valid integer",
                        "type": "int_type",
                    },
                ]
            },
        },
        "id": [123],
        "jsonrpc": "2.0",
    }
    assert echo.history == []