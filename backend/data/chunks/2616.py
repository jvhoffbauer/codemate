def test_security_http_digest():
    response = client.get("/users/me", headers={"Authorization": "Digest foobar"})
    assert response.status_code == 200, response.text
    assert response.json() == {"scheme": "Digest", "credentials": "foobar"}