def test_transaction_is_jsonrpc_method(
    probe,
    json_request,
    sentry_init,
    capture_exceptions,
    capture_events,
    assert_log_errors,
):
    sentry_init(send_default_pii=True)
    exceptions = capture_exceptions()
    events = capture_events()

    # Test in batch to ensure we correctly handle multiple requests
    json_request(
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

    assert {type(e) for e in exceptions} == {RuntimeError, ZeroDivisionError}

    assert_log_errors(
        "",
        pytest.raises(ZeroDivisionError),
        "",
        pytest.raises(RuntimeError),
    )

    assert set([e.get("transaction") for e in events]) == {
        "test_sentry.probe.<locals>.probe",
        "test_sentry.probe.<locals>.probe2",
    }