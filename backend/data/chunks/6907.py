def test_basic(json_request):
    resp = json_request(
        {
            "id": 1,
            "jsonrpc": "2.0",
            "method": "probe",
            "params": {"data": ["11", "22", "33"], "amount": 1000},
        }
    )
    assert resp == {"id": 1, "jsonrpc": "2.0", "result": [1011, 1022, 1033]}