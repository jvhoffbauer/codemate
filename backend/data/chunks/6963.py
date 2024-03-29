def test_method_no_auth(ep, raw_request, body):
    resp = raw_request(body)
    assert resp.status_code == 401
    assert resp.json() == {"detail": "Not authenticated"}