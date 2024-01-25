def test_custom_request_class_unexpected_type(ep, json_request):
    resp = json_request(
        {
            "id": 0,
            "jsonrpc": "2.0",
            "method": "probe",
            "params": {},
            "extra_value": {},
        }
    )
    assert resp == {
        "error": {
            "code": -32600,
            "message": "Invalid Request",
            "data": {
                "errors": [
                    {
                        "input": {},
                        "loc": ["extra_value"],
                        "msg": "Input should be a valid string",
                        "type": "string_type",
                    }
                ]
            },
        },
        "id": 0,
        "jsonrpc": "2.0",
    }