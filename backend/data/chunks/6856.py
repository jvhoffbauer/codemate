def test_batch(json_request):
    resp = json_request(
        [
            {
                "id": 111,
                "jsonrpc": "2.0",
                "method": "probe",
                "params": {"common": "one"},
            },
            {
                "id": 222,
                "jsonrpc": "2.0",
                "method": "probe",
                "params": {"common": "two"},
            },
            {
                "id": 333,
                "jsonrpc": "2.0",
                "method": "probe",
                "params": {"common": "three"},
            },
        ]
    )
    assert resp == [
        {"id": 111, "jsonrpc": "2.0", "result": ["shared-1", "one-1"]},
        {"id": 222, "jsonrpc": "2.0", "result": ["shared-1", "two-2"]},
        {"id": 333, "jsonrpc": "2.0", "result": ["shared-1", "three-3"]},
    ]