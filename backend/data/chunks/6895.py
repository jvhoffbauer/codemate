def test_request_params_missing(echo, json_request):
    resp = json_request(
        {
            "id": 0,
            "jsonrpc": "2.0",
            "method": "echo",
        }
    )
    assert resp == {
        "error": {
            "code": -32602,
            "message": "Invalid params",
            "data": {
                "errors": [
                    {
                        "input": None,
                        "loc": ["data"],
                        "msg": "Field required",
                        "type": "missing",
                    },
                ]
            },
        },
        "id": 0,
        "jsonrpc": "2.0",
    }
    assert echo.history == []