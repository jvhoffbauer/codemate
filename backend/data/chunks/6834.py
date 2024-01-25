def test_convert_error(ep, json_request, assert_log_errors):
    resp = json_request(
        {
            "id": 111,
            "jsonrpc": "2.0",
            "method": "convert_error",
            "params": {},
        }
    )

    assert resp == {
        "jsonrpc": "2.0",
        "id": 111,
        "error": {
            "code": 5002,
            "message": "My converted error",
        },
    }