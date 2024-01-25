def test_request_params_validation_error(echo, json_request):
    resp = json_request(
        {
            "id": 0,
            "jsonrpc": "2.0",
            "method": "echo",
            "params": 123,
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
                        "loc": ["params"],
                        "msg": "Input should be a valid dictionary",
                        "type": "dict_type",
                    }
                ]
            },
        },
        "id": 0,
        "jsonrpc": "2.0",
    }
    assert echo.history == []