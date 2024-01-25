def test_method_auth(ep, raw_request, body):
    resp = raw_request(body, auth=("user", "password"))
    assert resp.status_code == 200
    assert resp.json() == {"id": 1, "jsonrpc": "2.0", "result": "ok"}