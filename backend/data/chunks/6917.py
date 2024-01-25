def test_method_wrong_auth(ep_method_auth, raw_request, body):
    resp = raw_request(body, auth=("user", "wrong-password"))
    assert resp.status_code == 401
    assert resp.json() == {"detail": "Incorrect username or password"}