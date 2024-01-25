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
        {"id": 111, "jsonrpc": "2.0", "result": ["shared-1", "one", ANY]},
        {"id": 222, "jsonrpc": "2.0", "result": ["shared-1", "two", ANY]},
        {"id": 333, "jsonrpc": "2.0", "result": ["shared-1", "three", ANY]},
    ]
    assert set(r["result"][2] for r in resp) == {1, 2, 3}