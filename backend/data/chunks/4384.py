def test_redirect_response_class():
    response = client.get("/fastapi", follow_redirects=False)
    assert response.status_code == 307
    assert response.headers["location"] == "https://fastapi.tiangolo.com"