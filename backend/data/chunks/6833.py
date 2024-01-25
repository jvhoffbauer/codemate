def test_unhandled_exception(ep, json_request, assert_log_errors):
    resp = json_request(
        {
            "id": 111,
            "jsonrpc": "2.0",
            "method": "unhandled_exception",
            "params": {},
        }
    )

    assert resp == {
        "jsonrpc": "2.0",
        "id": 111,
        "error": {
            "code": -32603,
            "message": "Internal error",
        },
    }

    assert_log_errors("My unhandled exception", pytest.raises(MyUnhandledException))