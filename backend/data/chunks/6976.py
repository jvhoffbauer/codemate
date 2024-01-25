def test_single(method_request):
    resp1 = method_request("probe", {"common": "one"}, request_id=111)
    resp2 = method_request("probe", {"common": "two"}, request_id=222)
    resp3 = method_request("probe", {"common": "three"}, request_id=333)
    assert [resp1, resp2, resp3] == [
        {"id": 111, "jsonrpc": "2.0", "result": ["shared-1", "one", 1]},
        {"id": 222, "jsonrpc": "2.0", "result": ["shared-2", "two", 2]},
        {"id": 333, "jsonrpc": "2.0", "result": ["shared-3", "three", 3]},
    ]