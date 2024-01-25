def test_redirect_status_code():
    response = client.get("/pydantic", follow_redirects=False)
    assert response.status_code == 302
    assert response.headers["location"] == "https://pydantic-docs.helpmanual.io/"