def test_non_json__parse_error(echo, raw_request, content):
    resp = raw_request(content).json()
    assert resp == {
        "error": {
            "code": -32700,
            "message": "Parse error",
        },
        "id": None,
        "jsonrpc": "2.0",
    }
    assert echo.history == []