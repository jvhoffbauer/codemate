def test_single(ep, method_request):
    resp = method_request("probe", {"data": "one"}, request_id=111)
    assert resp == {"id": 111, "jsonrpc": "2.0", "result": "one"}
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
        ]
    }