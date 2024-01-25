def test_basic(probe, json_request):
    resp = json_request(
        {
            "id": 123,
            "jsonrpc": "2.0",
            "method": "probe",
            "params": {},
        }
    )
    assert resp == {"id": 123, "jsonrpc": "2.0", "result": "probe"}