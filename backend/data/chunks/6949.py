def test_custom_request_class(ep, json_request):
    resp = json_request(
        {
            "id": 0,
            "jsonrpc": "2.0",
            "method": "probe",
            "params": {},
            "extra_value": "test",
        }
    )
    assert resp == {"id": 0, "jsonrpc": "2.0", "result": "probe"}