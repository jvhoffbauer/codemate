def test_context_vars(ep, method_request):
    resp = method_request("probe_context_vars", {}, request_id=111)
    assert resp == {
        "id": 111,
        "jsonrpc": "2.0",
        "result": ["ep_middleware-value", "method_middleware-value"],
    }