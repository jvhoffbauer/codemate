def test_no_params(echo, json_request):
    resp = json_request(
        {
            "id": 111,
            "jsonrpc": "2.0",
            "method": "no_params",
        }
    )
    assert resp == {"id": 111, "jsonrpc": "2.0", "result": "123"}