def test_middleware_no_auth(ep_middleware_auth, raw_request, body):
    resp = raw_request(body)
    assert resp.status_code == 401
    assert resp.json() == {"detail": "Not authenticated"}