def test_unexpected_extra(ep, json_request):
    resp = json_request(
        {
            "id": 0,
            "jsonrpc": "2.0",
            "method": "echo",
            "params": {"data": "data-123"},
            "extra_value": "test",
            "unexpected_extra": 123,
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
                        "loc": ["unexpected_extra"],
                        "msg": "Extra inputs are not permitted",
                        "type": "extra_forbidden",
                    },
                ]
            },
        },
        "id": 0,
        "jsonrpc": "2.0",
    }