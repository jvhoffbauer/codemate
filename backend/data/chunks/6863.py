def test_basic(json_request):
    resp = json_request(
        {
            "id": 1,
            "jsonrpc": "2.0",
            "method": "probe1",
            "params": {
                "data": [
                    {"amount": 1, "currency": "USD"},
                    {"amount": 2, "currency": "RUB"},
                ]
            },
        }
    )
    assert resp == {
        "id": 1,
        "jsonrpc": "2.0",
        "result": [
            {"amount": 1, "currency": "USD"},
            {"amount": 2, "currency": "RUB"},
        ],
    }

    resp = json_request(
        {
            "id": 1,
            "jsonrpc": "2.0",
            "method": "probe2",
            "params": {
                "data": [
                    {"amount": 3, "currency": "USD"},
                    {"amount": 4, "currency": "RUB"},
                ]
            },
        }
    )
    assert resp == {
        "id": 1,
        "jsonrpc": "2.0",
        "result": [
            {"amount": 3, "currency": "USD"},
            {"amount": 4, "currency": "RUB"},
        ],
    }