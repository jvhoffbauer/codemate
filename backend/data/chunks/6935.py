def test_batch(probe, json_request):
    resp = json_request(
        [
            {
                "id": 1,
                "jsonrpc": "2.0",
                "method": "probe",
                "params": {},
            },
            {
                "id": 2,
                "jsonrpc": "2.0",
                "method": "probe2",
                "params": {},
            },
        ]
    )
    assert resp == [
        {"id": 1, "jsonrpc": "2.0", "result": "probe"},
        {"id": 2, "jsonrpc": "2.0", "result": "probe2"},
    ]