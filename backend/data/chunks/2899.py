def test_security_http_bearer_incorrect_scheme_credentials():
    response = client.get("/users/me", headers={"Authorization": "Basic notreally"})
    assert response.status_code == 403, response.text
    assert response.json() == {"detail": "Invalid authentication credentials"}