def test_deep_data_validation(echo, json_request):
    resp = json_request(
        {
            "id": 0,
            "jsonrpc": "2.0",
            "method": "deep_data",
            "params": {"data": [{}]},
        }
    )
    assert resp == {
        "error": {
            "code": -32602,
            "message": "Invalid params",
            "data": {
                "errors": [
                    {
                        "input": {},
                        "loc": ["data", 0, "inner_data"],
                        "msg": "Field required",
                        "type": "missing",
                    },
                ]
            },
        },
        "id": 0,
        "jsonrpc": "2.0",
    }