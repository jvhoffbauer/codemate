def test_ep_exception(ep, method_request, assert_log_errors):
    resp = method_request("probe", {"data": "one"}, request_id=111)
    assert resp == {
        "id": 111,
        "jsonrpc": "2.0",
        "error": {"code": -32603, "message": "Internal error"},
    }
    assert ep.calls == {
        111: [
            (
                "mw_first",
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
                "mw_exception_exit",
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
                "mw_last",
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
                "mw_last",
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
                "mw_exception_exit",
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
                "mw_first",
                "exit",
                {
                    "id": 111,
                    "jsonrpc": "2.0",
                    "method": "probe",
                    "params": {"data": "one"},
                },
                {
                    "id": 111,
                    "jsonrpc": "2.0",
                    "error": {"code": -32603, "message": "Internal error"},
                },
                RuntimeError,
            ),
        ]
    }

    assert_log_errors(unique_marker, pytest.raises(RuntimeError))