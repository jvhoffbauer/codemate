def test_batch(ep, json_request):
    resp = json_request(
        [
            {
                "id": 111,
                "jsonrpc": "2.0",
                "method": "probe",
                "params": {"data": "one"},
            },
            {
                "id": 222,
                "jsonrpc": "2.0",
                "method": "probe",
                "params": {"data": "two"},
            },
        ]
    )
    assert resp == [
        {"id": 111, "jsonrpc": "2.0", "result": "one"},
        {"id": 222, "jsonrpc": "2.0", "result": "two"},
    ]
    assert ep.calls == {
        111: [
            (
                "ep_middleware",
                "enter",
                {
                    "id": 111,
                    "jsonrpc": "2.0",
                    "method": "probe",
                    "params": {"data": "one"},
                },
                None,
                None,
            ),
            (
                "method_middleware",
                "enter",
                {
                    "id": 111,
                    "jsonrpc": "2.0",
                    "method": "probe",
                    "params": {"data": "one"},
                },
                None,
                None,
            ),
            (
                "method_middleware",
                "exit",
                {
                    "id": 111,
                    "jsonrpc": "2.0",
                    "method": "probe",
                    "params": {"data": "one"},
                },
                {"id": 111, "jsonrpc": "2.0", "result": "one"},
                None,
            ),
            (
                "ep_middleware",
                "exit",
                {
                    "id": 111,
                    "jsonrpc": "2.0",
                    "method": "probe",
                    "params": {"data": "one"},
                },
                {"id": 111, "jsonrpc": "2.0", "result": "one"},
                None,
            ),
        ],
        222: [
            (
                "ep_middleware",
                "enter",
                {
                    "id": 222,
                    "jsonrpc": "2.0",
                    "method": "probe",
                    "params": {"data": "two"},
                },
                None,
                None,
            ),
            (
                "method_middleware",
                "enter",
                {
                    "id": 222,
                    "jsonrpc": "2.0",
                    "method": "probe",
                    "params": {"data": "two"},
                },
                None,
                None,
            ),
            (
                "method_middleware",
                "exit",
                {
                    "id": 222,
                    "jsonrpc": "2.0",
                    "method": "probe",
                    "params": {"data": "two"},
                },
                {"id": 222, "jsonrpc": "2.0", "result": "two"},
                None,
            ),
            (
                "ep_middleware",
                "exit",
                {
                    "id": 222,
                    "jsonrpc": "2.0",
                    "method": "probe",
                    "params": {"data": "two"},
                },
                {"id": 222, "jsonrpc": "2.0", "result": "two"},
                None,
            ),
        ],
    }