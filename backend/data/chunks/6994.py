def test_batch_error(ep, json_request, assert_log_errors):
    resp = json_request(
        [
            {
                "id": 111,
                "jsonrpc": "2.0",
                "method": "probe_error",
                "params": {"data": "one"},
            },
            {
                "id": 222,
                "jsonrpc": "2.0",
                "method": "probe_error",
                "params": {"data": "two"},
            },
        ]
    )
    assert resp == [
        {
            "id": 111,
            "jsonrpc": "2.0",
            "error": {
                "code": 33333,
                "data": unique_marker2,
                "message": "Test error",
            },
        },
        {
            "id": 222,
            "jsonrpc": "2.0",
            "error": {
                "code": 33333,
                "data": unique_marker2,
                "message": "Test error",
            },
        },
    ]
    assert ep.calls == {
        111: [
            (
                "ep_middleware",
                "enter",
                {
                    "id": 111,
                    "jsonrpc": "2.0",
                    "method": "probe_error",
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
                    "method": "probe_error",
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
                    "method": "probe_error",
                    "params": {"data": "one"},
                },
                {
                    "id": 111,
                    "jsonrpc": "2.0",
                    "error": {"code": -32603, "message": "Internal error"},
                },
                RuntimeError,
            ),
            (
                "ep_middleware",
                "exit",
                {
                    "id": 111,
                    "jsonrpc": "2.0",
                    "method": "probe_error",
                    "params": {"data": "one"},
                },
                {
                    "id": 111,
                    "jsonrpc": "2.0",
                    "error": {"code": -32603, "message": "Internal error"},
                },
                RuntimeError,
            ),
        ],
        222: [
            (
                "ep_middleware",
                "enter",
                {
                    "id": 222,
                    "jsonrpc": "2.0",
                    "method": "probe_error",
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
                    "method": "probe_error",
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
                    "method": "probe_error",
                    "params": {"data": "two"},
                },
                {
                    "id": 222,
                    "jsonrpc": "2.0",
                    "error": {"code": -32603, "message": "Internal error"},
                },
                RuntimeError,
            ),
            (
                "ep_middleware",
                "exit",
                {
                    "id": 222,
                    "jsonrpc": "2.0",
                    "method": "probe_error",
                    "params": {"data": "two"},
                },
                {
                    "id": 222,
                    "jsonrpc": "2.0",
                    "error": {"code": -32603, "message": "Internal error"},
                },
                RuntimeError,
            ),
        ],
    }

    assert_log_errors(
        unique_marker,
        pytest.raises(RuntimeError),
        unique_marker,
        pytest.raises(RuntimeError),
    )