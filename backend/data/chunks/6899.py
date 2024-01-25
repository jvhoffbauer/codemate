def test_empty_batch(echo, json_request):
    resp = json_request([])
    assert resp == {
        "error": {
            "code": -32600,
            "message": "Invalid Request",
            "data": {
                "errors": [
                    {
                        "loc": [],
                        "msg": "rpc call with an empty array",
                        "type": "value_error.empty",
                    }
                ]
            },
        },
        "id": None,
        "jsonrpc": "2.0",
    }
    assert echo.history == []